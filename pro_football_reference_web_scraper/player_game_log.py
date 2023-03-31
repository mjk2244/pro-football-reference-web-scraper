import pandas as pd  # type: ignore
from bs4 import BeautifulSoup
import requests


# function that returns a player's game log in a given season
# player: player's full name (e.g. Tom Brady)
# position: abbreviation (QB, RB, WR, TE only)
def get_player_game_log(player: str, position: str, season: int) -> pd.DataFrame:
    """A function to retrieve a player's game log in a given season.

    Returns a pandas DataFrame of a NFL player's game log in a given season, including position-specific statistics.

    Args:
        player (str): A NFL player's full name, as it appears on Pro Football Reference
        position (str): The position the player plays. Must be 'QB', 'RB', 'WR', or 'TE'
        season (int): The season of the game log you are trying to retrieve

    Returns:
        pandas.DataFrame: Each game is a row

    """
    # make request to find proper href
    r1 = make_request_list(player, position, season)
    player_list = get_soup(r1)

    # find href
    href = get_href(player, position, season, player_list)

    # make HTTP request and extract HTML
    r2 = make_request_player(href, season)

    # parse HTML using BeautifulSoup
    game_log = get_soup(r2)

    # generating the appropriate game log format according to position
    if 'QB' in position:
        return qb_game_log(game_log)
    elif 'WR' in position or 'TE' in position:
        return wr_game_log(game_log)
    elif 'RB' in position:
        return rb_game_log(game_log)


# helper function that gets the player's href
def get_href(player: str, position: str, season: int, player_list: BeautifulSoup) -> str:
    players = player_list.find('div', id='div_players').find_all('p')
    for p in players:
        seasons = p.text.split(' ')
        seasons = seasons[len(seasons) - 1].split('-')
        if season >= int(seasons[0]) and season <= int(seasons[1]) and player in p.text and position in p.text:
            href = p.find('a').get('href')
    return href


# helper function that makes a HTTP request over a list of players with a given last initial
def make_request_list(player: str, position: str, season: int):
    name_split = player.split(' ')
    last_initial = name_split[1][0]
    url = 'https://www.pro-football-reference.com/players/%s/' % (last_initial)
    return requests.get(url)


# helper function that makes a HTTP request for a given player's game log
def make_request_player(href: str, season: int):
    url = 'https://www.pro-football-reference.com%s/gamelog/%s/' % (href, season)
    return requests.get(url)


# helper function that takes a requests.Response object and returns a BeautifulSoup object
def get_soup(request):
    return BeautifulSoup(request.text, 'html.parser')


# helper function that takes a BeautifulSoup object and converts it into a pandas dataframe containing a QB game log
def qb_game_log(soup: BeautifulSoup) -> pd.DataFrame:
    # Most relevant QB stats, in my opinion. Could adjust if necessary
    data = {
        'Date': [],
        'Week': [],
        'Team': [],
        'Game_Location': [],
        'Opp': [],
        'Result': [],
        'Cmp': [],
        'Att': [],
        'Pass_Yds': [],
        'Pass_TD': [],
        'Int': [],
        'Rating': [],
        'Sacked': [],
        'Rush_Att': [],
        'Rush_Yds': [],
        'Rush_TD': [],
    }  # type: dict

    table_rows = soup.find('tbody').find_all('tr')

    # ignore inactive or DNP games
    to_ignore = []
    for i in range(len(table_rows)):
        elements = table_rows[i].find_all('td')
        if elements[len(elements) - 1].text == 'Inactive' or elements[len(elements) - 1].text == 'Did Not Play':
            to_ignore.append(i)

    # adding data to data dictionary
    for i in range(len(table_rows)):
        if i not in to_ignore:
            data['Date'].append(table_rows[i].find('td', {'data-stat': 'game_date'}).text)
            data['Week'].append(int(table_rows[i].find('td', {'data-stat': 'week_num'}).text))
            data['Team'].append(table_rows[i].find('td', {'data-stat': 'team'}).text)
            data['Game_Location'].append(table_rows[i].find('td', {'data-stat': 'game_location'}).text)
            data['Opp'].append(table_rows[i].find('td', {'data-stat': 'opp'}).text)
            data['Result'].append(table_rows[i].find('td', {'data-stat': 'game_result'}).text)
            data['Cmp'].append(int(table_rows[i].find('td', {'data-stat': 'pass_cmp'}).text))
            data['Att'].append(int(table_rows[i].find('td', {'data-stat': 'pass_att'}).text))
            data['Pass_Yds'].append(int(table_rows[i].find('td', {'data-stat': 'pass_yds'}).text))
            data['Pass_TD'].append(int(table_rows[i].find('td', {'data-stat': 'pass_td'}).text))
            data['Int'].append(int(table_rows[i].find('td', {'data-stat': 'pass_int'}).text))
            data['Rating'].append(float(table_rows[i].find('td', {'data-stat': 'pass_rating'}).text))
            data['Sacked'].append(int(table_rows[i].find('td', {'data-stat': 'pass_sacked'}).text))
            data['Rush_Att'].append(int(table_rows[i].find('td', {'data-stat': 'rush_att'}).text))
            data['Rush_Yds'].append(int(table_rows[i].find('td', {'data-stat': 'rush_yds'}).text))
            data['Rush_TD'].append(int(table_rows[i].find('td', {'data-stat': 'rush_td'}).text))

    return pd.DataFrame(data=data)


# helper function that takes a BeautifulSoup object and converts it into a pandas dataframe containing a WR/TE game log
def wr_game_log(soup: BeautifulSoup) -> pd.DataFrame:
    # Most relevant WR stats, in my opinion.
    # Could adjust if necessary (maybe figure out how to incorporate rushing stats?)

    data = {
        'Date': [],
        'Week': [],
        'Team': [],
        'Game_Location': [],
        'Opp': [],
        'Result': [],
        'Tgt': [],
        'Rec': [],
        'Rec_Yds': [],
        'Rec_TD': [],
        'Snap_Pct': [],
    }  # type: dict

    table_rows = soup.find('tbody').find_all('tr')

    # ignore inactive or DNP games
    to_ignore = []
    for i in range(len(table_rows)):
        elements = table_rows[i].find_all('td')
        if elements[len(elements) - 1].text == 'Inactive' or elements[len(elements) - 1].text == 'Did Not Play':
            to_ignore.append(i)

    # adding data to data dictionray
    for i in range(len(table_rows)):
        if i not in to_ignore:
            data['Date'].append(table_rows[i].find('td', {'data-stat': 'game_date'}).text)
            data['Week'].append(int(table_rows[i].find('td', {'data-stat': 'week_num'}).text))
            data['Team'].append(table_rows[i].find('td', {'data-stat': 'team'}).text)
            data['Game_Location'].append(table_rows[i].find('td', {'data-stat': 'game_location'}).text)
            data['Opp'].append(table_rows[i].find('td', {'data-stat': 'opp'}).text)
            data['Result'].append(table_rows[i].find('td', {'data-stat': 'game_result'}).text)
            data['Tgt'].append(int(table_rows[i].find('td', {'data-stat': 'targets'}).text))
            data['Rec'].append(int(table_rows[i].find('td', {'data-stat': 'rec'}).text))
            data['Rec_Yds'].append(int(table_rows[i].find('td', {'data-stat': 'rec_yds'}).text))
            data['Rec_TD'].append(int(table_rows[i].find('td', {'data-stat': 'rec_td'}).text))
            data['Snap_Pct'].append(float(int(table_rows[i].find('td', {'data-stat': 'off_pct'}).text[:-1]) / 100))

    return pd.DataFrame(data=data)


def rb_game_log(soup: BeautifulSoup) -> pd.DataFrame:
    # Most relevant RB stats, in my opinion. Could adjust if necessary
    data = {
        'Date': [],
        'Week': [],
        'Team': [],
        'Game_Location': [],
        'Opp': [],
        'Result': [],
        'Rush_Att': [],
        'Rush_Yds': [],
        'Rush_TD': [],
        'Tgt': [],
        'Rec_Yds': [],
        'Rec_TD': [],
    }  # type: dict

    table_rows = soup.find('tbody').find_all('tr')

    # ignore inactive or DNP games
    to_ignore = []
    for i in range(len(table_rows)):
        elements = table_rows[i].find_all('td')
        if elements[len(elements) - 1].text == 'Inactive' or elements[len(elements) - 1].text == 'Did Not Play':
            to_ignore.append(i)

    # adding data to data dictionary
    for i in range(len(table_rows)):
        if i not in to_ignore:
            data['Date'].append(table_rows[i].find('td', {'data-stat': 'game_date'}).text)
            data['Week'].append(int(table_rows[i].find('td', {'data-stat': 'week_num'}).text))
            data['Team'].append(table_rows[i].find('td', {'data-stat': 'team'}).text)
            data['Game_Location'].append(table_rows[i].find('td', {'data-stat': 'game_location'}).text)
            data['Opp'].append(table_rows[i].find('td', {'data-stat': 'opp'}).text)
            data['Result'].append(table_rows[i].find('td', {'data-stat': 'game_result'}).text)
            data['Rush_Att'].append(int(table_rows[i].find('td', {'data-stat': 'rush_att'}).text))
            data['Rush_Yds'].append(int(table_rows[i].find('td', {'data-stat': 'rush_yds'}).text))
            data['Rush_TD'].append(int(table_rows[i].find('td', {'data-stat': 'rush_td'}).text))
            data['Tgt'].append(int(table_rows[i].find('td', {'data-stat': 'targets'}).text))
            data['Rec_Yds'].append(int(table_rows[i].find('td', {'data-stat': 'rec_yds'}).text))
            data['Rec_TD'].append(int(table_rows[i].find('td', {'data-stat': 'rec_td'}).text))

    return pd.DataFrame(data=data)
