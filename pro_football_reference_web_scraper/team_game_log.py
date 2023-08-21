from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date
from haversine import haversine, Unit

# TODO: add older teams to this list
team_hrefs = {
    'Arizona Cardinals': 'crd',
    'Baltimore Colts': 'clt',
    'St. Louis Cardinals': 'crd',
    'Boston Patriots': 'nwe',
    'Chicago Bears': 'chi',
    'Green Bay Packers': 'gnb',
    'New York Giants': 'nyg',
    'Detroit Lions': 'det',
    'Washington Commanders': 'was',
    'Washington Football Team': 'was',
    'Washington Redskins': 'was',
    'Philadelphia Eagles': 'phi',
    'Pittsburgh Steelers': 'pit',
    'Los Angeles Chargers': 'sdg',
    'San Francisco 49ers': 'sfo',
    'Houston Oilers': 'oti',
    'Cleveland Browns': 'cle',
    'Indianapolis Colts': 'clt',
    'Dallas Cowboys': 'dal',
    'Kansas City Chiefs': 'kan',
    'Los Angeles Rams': 'ram',
    'Denver Broncos': 'den',
    'New York Jets': 'nyj',
    'New England Patriots': 'nwe',
    'Las Vegas Raiders': 'rai',
    'Tennessee Titans': 'oti',
    'Tennessee Oilers': 'oti',
    'Phoenix Cardinals': 'crd',
    'Los Angeles Raiders': 'rai',
    'Buffalo Bills': 'buf',
    'Minnesota Vikings': 'min',
    'Atlanta Falcons': 'atl',
    'Miami Dolphins': 'mia',
    'New Orleans Saints': 'nor',
    'Cincinnati Bengals': 'cin',
    'Seattle Seahawks': 'sea',
    'Tampa Bay Buccaneers': 'tam',
    'Carolina Panthers': 'car',
    'Jacksonville Jaguars': 'jax',
    'Baltimore Ravens': 'rav',
    'Houston Texans': 'htx',
    'Oakland Raiders': 'rai',
    'San Diego Chargers': 'sdg',
    'St. Louis Rams': 'ram',
    'Boston Patriots': 'nwe',
}

months = {"September": 9, "October": 10, "November": 11, "December": 12, "January": 1}

locations = {
    'Boston': {'latitude': 42.3656, 'longitude': 71.0096, 'airport': 'BOS'},
    'Phoenix': {'latitude': 33.4352, 'longitude': 112.0101, 'airport': 'PHX'},
    'Chicago': {'latitude': 41.9803, 'longitude': 87.9090, 'airport': 'ORD'},
    'Green Bay': {'latitude': 44.4923, 'longitude': 88.1278, 'airport': 'GRB'},
    'New York': {'latitude': 40.6895, 'longitude': 74.1745, 'airport': 'EWR'},
    'Detroit': {'latitude': 42.2162, 'longitude': 83.3554, 'airport': 'DTW'},
    'Washington DC': {'latitude': 38.9531, 'longitude': 77.4565, 'airport': 'IAD'},
    'Philadelphia': {'latitude': 39.9526, 'longitude': 75.1652, 'airport': 'PHL'},
    'Pittsburgh': {'latitude': 40.4919, 'longitude': 80.2352, 'airport': 'PIT'},
    'Los Angeles': {'latitude': 33.9416, 'longitude': 118.4085, 'airport': 'LAX'},
    'San Francisco': {'latitude': 37.3639, 'longitude': 121.9289, 'airport': 'SJC'},
    'Cleveland': {'latitude': 41.4058, 'longitude': 81.8539, 'airport': 'CLE'},
    'Indianapolis': {'latitude': 39.7169, 'longitude': 86.2956, 'airport': 'IND'},
    'Dallas': {'latitude': 32.8998, 'longitude': 97.0403, 'airport': 'DFW'},
    'Kansas City': {'latitude': 39.3036, 'longitude': 94.7093, 'airport': 'MCI'},
    'Denver': {'latitude': 39.8564, 'longitude': 104.6764, 'airport': 'DEN'},
    'Providence': {'latitude': 41.7235, 'longitude': 71.4270, 'airport': 'PVD'},
    'Las Vegas': {'latitude': 36.0840, 'longitude': 115.1537, 'airport': 'LAS'},
    'Nashville': {'latitude': 36.1263, 'longitude': 86.6774, 'airport': 'BNA'},
    'Buffalo': {'latitude': 42.9397, 'longitude': 78.7295, 'airport': 'BUF'},
    'Minneapolis': {'latitude': 44.8848, 'longitude': 93.2223, 'airport': 'MSP'},
    'Atlanta': {'latitude': 33.6407, 'longitude': 84.4277, 'airport': 'ATL'},
    'Miami': {'latitude': 26.0742, 'longitude': 80.1506, 'airport': 'FLL'},
    'New Orleans': {'latitude': 29.9911, 'longitude': 90.2592, 'airport': 'MSY'},
    'Cincinnati': {'latitude': 39.0508, 'longitude': 84.6673, 'airport': 'CVG'},
    'Seattle': {'latitude': 47.4480, 'longitude': 122.3088, 'airport': 'SEA'},
    'Tampa Bay': {'latitude': 27.9772, 'longitude': 82.5311, 'airport': 'TPA'},
    'Charlotte': {'latitude': 35.2144, 'longitude': 80.9473, 'airport': 'CLT'},
    'Jacksonville': {'latitude': 30.4941, 'longitude': 81.6879, 'airport': 'JAX'},
    'Baltimore': {'latitude': 39.1774, 'longitude': 76.6684, 'airport': 'BWI'},
    'Houston': {'latitude': 29.9902, 'longitude': 95.3368, 'airport': 'IAH'},
    'Oakland': {'latitude': 37.7126, 'longitude': 122.2197, 'airport': 'OAK'},
    'San Diego': {'latitude': 32.7338, 'longitude': 117.1933, 'airport': 'SAN'},
    'St. Louis': {'latitude': 38.7499, 'longitude': 90.3748, 'airport': 'STL'},
}

cities = {
    'Arizona Cardinals': 'Phoenix',
    'Chicago Bears': 'Chicago',
    'Green Bay Packers': 'Green Bay',
    'New York Giants': 'New York',
    'Detroit Lions': 'Detroit',
    'Washington Commanders': 'Washington DC',
    'Washington Football Team': 'Washington DC',
    'Washington Redskins': 'Washington DC',
    'Philadelphia Eagles': 'Philadelphia',
    'Pittsburgh Steelers': 'Pittsburgh',
    'Los Angeles Chargers': 'Los Angeles',
    'San Francisco 49ers': 'San Francisco',
    'Houston Oilers': 'Houston',
    'Cleveland Browns': 'Cleveland',
    'Indianapolis Colts': 'Indianapolis',
    'Dallas Cowboys': 'Dallas',
    'Kansas City Chiefs': 'Kansas City',
    'Los Angeles Rams': 'Los Angeles',
    'Denver Broncos': 'Denver',
    'New York Jets': 'New York',
    'New England Patriots': 'Providence',
    'Las Vegas Raiders': 'Las Vegas',
    'Tennessee Titans': 'Nashville',
    'Tennessee Oilers': 'Nashville',
    'Phoenix Cardinals': 'Phoenix',
    'Los Angeles Raiders': 'Los Angeles',
    'Buffalo Bills': 'Buffalo',
    'Minnesota Vikings': 'Minneapolis',
    'Atlanta Falcons': 'Atlanta',
    'Miami Dolphins': 'Miami',
    'New Orleans Saints': 'New Orleans',
    'Cincinnati Bengals': 'Cincinnati',
    'Seattle Seahawks': 'Seattle',
    'Tampa Bay Buccaneers': 'Tampa Bay',
    'Carolina Panthers': 'Charlotte',
    'Jacksonville Jaguars': 'Jacksonville',
    'Baltimore Ravens': 'Baltimore',
    'Houston Texans': 'Houston',
    'Oakland Raiders': 'Oakland',
    'San Diego Chargers': 'San Diego',
    'St. Louis Rams': 'St. Louis',
    'Baltimore Colts': 'Baltimore',
    'St. Louis Cardinals': 'St. Louis',
    'Boston Patriots': 'Boston',
}


# function that returns a team's game log in a given season
def get_team_game_log(team: str, season: int) -> pd.DataFrame:
    """A function to retrieve a team's game log in a given season.

    Returns a pandas DataFrame of a NFL team's game log in a given season, including relevant team-level statistics.

    Args:
        team (str): A NFL team's name, as it appears on Pro Football Reference
        season (int): The season of the game log you are trying to retrieve

    Returns:
        pandas.DataFrame: Each game is a row of the DataFrame

    """

    # raise exception if team name is misspelled
    if team not in team_hrefs.keys():
        raise Exception('Invalid team name. Note: spelling is case sensitive')

    # make HTTP request and extract HTML
    r = make_request(team, season)

    if r.status_code == 404:
        raise Exception('404 error. The ' + team + ' may not have existed in ' + str(season))

    # parse HTML using BeautifulSoup
    soup = get_soup(r)

    # collect data and return data frame
    return collect_data(soup, season, team)


def make_request(team: str, season: int):
    url = 'https://www.pro-football-reference.com/teams/%s/%s.htm' % (team_hrefs[team], str(season))
    return requests.get(url)


def get_soup(request) -> BeautifulSoup:
    return BeautifulSoup(request.text, 'html.parser')


def collect_data(soup: BeautifulSoup, season: int, team: str) -> pd.DataFrame:
    # set up data frame
    data = {
        'week': [],
        'day': [],
        'rest_days': [],
        'home_team': [],
        'distance_travelled': [],
        'opp': [],
        'result': [],
        'points_for': [],
        'points_allowed': [],
        'tot_yds': [],
        'pass_yds': [],
        'rush_yds': [],
        'opp_tot_yds': [],
        'opp_pass_yds': [],
        'opp_rush_yds': [],
    }
    df = pd.DataFrame(data)

    # loading game data
    games = soup.find_all('tbody')[1].find_all('tr')

    # remove playoff games
    j = 0
    while j < len(games) and games[j].find('td', {'data-stat': 'game_date'}).text != 'Playoffs':
        j += 1
    for k in range(j, len(games)):
        games.pop()

    # remove bye weeks
    bye_weeks = []
    for j in range(len(games)):
        if games[j].find('td', {'data-stat': 'opp'}).text == 'Bye Week':
            bye_weeks.append(j)

    if len(bye_weeks) > 1:
        games.pop(bye_weeks[0])
        games.pop(bye_weeks[1] - 1)

    elif len(bye_weeks) == 1:
        games.pop(bye_weeks[0])

    # remove canceled games
    to_delete = []
    for j in range(len(games)):
        if games[j].find('td', {'data-stat': 'boxscore_word'}).text == 'canceled':
            to_delete.append(j)
    for k in to_delete:
        games.pop(k)

    # gathering data
    for i in range(len(games)):
        week = int(games[i].find('th', {'data-stat': 'week_num'}).text)
        day = games[i].find('td', {'data-stat': 'game_day_of_week'}).text
        if i > 0:
            if games[i - 1].find('td', {'data-stat': 'opp'}).text == 'Bye Week':
                date1 = games[i - 2].find('td', {'data-stat': 'game_date'}).text.split(' ')
                date2 = games[i].find('td', {'data-stat': 'game_date'}).text.split(' ')
            else:
                date1 = games[i - 1].find('td', {'data-stat': 'game_date'}).text.split(' ')
                date2 = games[i].find('td', {'data-stat': 'game_date'}).text.split(' ')
            if date1[0] == 'January':
                rest_days = date(season + 1, months[date2[0]], int(date2[1])) - date(
                    season + 1, months[date1[0]], int(date1[1])
                )
            elif date2[0] == 'January':
                rest_days = date(season + 1, months[date2[0]], int(date2[1])) - date(
                    season, months[date1[0]], int(date1[1])
                )
            else:
                rest_days = date(season + 1, months[date2[0]], int(date2[1])) - date(
                    season + 1, months[date1[0]], int(date1[1])
                )
        else:
            rest_days = date(2022, 7, 11) - date(2022, 7, 1)  # setting first game as 10 rest days

        opp = games[i].find('td', {'data-stat': 'opp'}).text

        if games[i].find('td', {'data-stat': 'game_location'}).text == '@':
            home_team = False
            distance_travelled = calculate_distance(locations[cities[team]], locations[cities[opp]])
        else:
            home_team = True
            distance_travelled = 0

        result = games[i].find('td', {'data-stat': 'game_outcome'}).text
        points_for = int(games[i].find('td', {'data-stat': 'pts_off'}).text)
        points_allowed = int(games[i].find('td', {'data-stat': 'pts_def'}).text)
        tot_yds = int(games[i].find('td', {'data-stat': 'yards_off'}).text)
        pass_yds = int(games[i].find('td', {'data-stat': 'pass_yds_off'}).text)
        rush_yds = int(games[i].find('td', {'data-stat': 'rush_yds_off'}).text)
        opp_tot_yds = int(games[i].find('td', {'data-stat': 'yards_def'}).text)
        opp_pass_yds = int(games[i].find('td', {'data-stat': 'pass_yds_def'}).text)
        opp_rush_yds = int(games[i].find('td', {'data-stat': 'rush_yds_def'}).text)

        # add row to data frame
        df.loc[len(df.index)] = [
            week,
            day,
            rest_days,
            home_team,
            distance_travelled,
            opp,
            result,
            points_for,
            points_allowed,
            tot_yds,
            pass_yds,
            rush_yds,
            opp_tot_yds,
            opp_pass_yds,
            opp_rush_yds,
        ]

    return df


def calculate_distance(city1: dict, city2: dict) -> float:
    coordinates1 = (city1['latitude'], city1['longitude'])
    coordinates2 = (city2['latitude'], city2['longitude'])
    return haversine(coordinates1, coordinates2, unit=Unit.MILES)
