import pandas as pd  # type: ignore
from bs4 import BeautifulSoup
import requests

valid_positions = ['QB', 'RB', 'WR', 'TE']


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
        pandas.DataFrame: Each game is a row of the DataFrame

    """

    # position arg must be formatted properly
    if position not in valid_positions:
        raise Exception('Invalid position: "position" arg must be "QB", "RB", "WR", or "TE"')

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
        return wr_game_log(game_log, season)
    elif 'RB' in position:
        return rb_game_log(game_log)


# helper function that gets the player's href
def get_href(player: str, position: str, season: int, player_list: BeautifulSoup) -> str:
    players = player_list.find('div', id='div_players').find_all('p')
    for p in players:
        seasons = p.text.split(' ')
        seasons = seasons[len(seasons) - 1].split('-')
        if season >= int(seasons[0]) and season <= int(seasons[1]) and player in p.text and position in p.text:
            return p.find('a').get('href').replace('.htm', '')
    raise Exception('Cannot find a ' + position + ' named ' + player + ' from ' + str(season))


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
        'date': [],
        'week': [],
        'team': [],
        'game_location': [],
        'opp': [],
        'result': [],
        'team_pts': [],
        'opp_pts': [],
        'cmp': [],
        'att': [],
        'pass_yds': [],
        'pass_td': [],
        'int': [],
        'rating': [],
        'sacked': [],
        'rush_att': [],
        'rush_yds': [],
        'rush_td': [],
    }  # type: dict

    table_rows = soup.find('tbody').find_all('tr')

    # ignore inactive or DNP games
    to_ignore = []
    for i in range(len(table_rows)):
        elements = table_rows[i].find_all('td')
        x = elements[len(elements) - 1].text
        if x == 'Inactive' or x == 'Did Not Play' or x == 'Injured Reserve':
            to_ignore.append(i)

    # adding data to data dictionary
    for i in range(len(table_rows)):
        if i not in to_ignore:
            data['date'].append(table_rows[i].find('td', {'data-stat': 'game_date'}).text)
            data['week'].append(int(table_rows[i].find('td', {'data-stat': 'week_num'}).text))
            data['team'].append(table_rows[i].find('td', {'data-stat': 'team'}).text)
            data['game_location'].append(table_rows[i].find('td', {'data-stat': 'game_location'}).text)
            data['opp'].append(table_rows[i].find('td', {'data-stat': 'opp'}).text)
            data['result'].append(table_rows[i].find('td', {'data-stat': 'game_result'}).text.split(' ')[0])
            data['team_pts'].append(
                int(table_rows[i].find('td', {'data-stat': 'game_result'}).text.split(' ')[1].split('-')[0])
            )
            data['opp_pts'].append(
                int(table_rows[i].find('td', {'data-stat': 'game_result'}).text.split(' ')[1].split('-')[1])
            )
            data['cmp'].append(int(table_rows[i].find('td', {'data-stat': 'pass_cmp'}).text)) if table_rows[i].find(
                'td', {'data-stat': 'pass_cmp'}
            ).text != '' else data['cmp'].append(0)
            data['att'].append(int(table_rows[i].find('td', {'data-stat': 'pass_att'}).text)) if table_rows[i].find(
                'td', {'data-stat': 'pass_att'}
            ).text != '' else data['att'].append(0)
            data['pass_yds'].append(int(table_rows[i].find('td', {'data-stat': 'pass_yds'}).text)) if table_rows[
                i
            ].find('td', {'data-stat': 'pass_yds'}).text != '' else data['pass_yds'].append(0)
            data['pass_td'].append(int(table_rows[i].find('td', {'data-stat': 'pass_td'}).text)) if table_rows[i].find(
                'td', {'data-stat': 'pass_td'}
            ).text != '' else data['pass_td'].append(0)
            data['int'].append(int(table_rows[i].find('td', {'data-stat': 'pass_int'}).text)) if table_rows[i].find(
                'td', {'data-stat': 'pass_int'}
            ).text != '' else data['int'].append(0)
            data['rating'].append(float(table_rows[i].find('td', {'data-stat': 'pass_rating'}).text)) if table_rows[
                i
            ].find('td', {'data-stat': 'pass_rating'}).text != '' else data['rating'].append(0)
            data['sacked'].append(int(table_rows[i].find('td', {'data-stat': 'pass_sacked'}).text)) if table_rows[
                i
            ].find('td', {'data-stat': 'pass_sacked'}).text != '' else data['sacked'].append(0)
            data['rush_att'].append(int(table_rows[i].find('td', {'data-stat': 'rush_att'}).text)) if table_rows[
                i
            ].find('td', {'data-stat': 'rush_att'}).text != '' else data['rush_att'].append(0)
            data['rush_yds'].append(int(table_rows[i].find('td', {'data-stat': 'rush_yds'}).text)) if table_rows[
                i
            ].find('td', {'data-stat': 'rush_yds'}).text != '' else data['rush_yds'].append(0)
            data['rush_td'].append(int(table_rows[i].find('td', {'data-stat': 'rush_td'}).text)) if table_rows[i].find(
                'td', {'data-stat': 'rush_td'}
            ).text != '' else data['rush_td'].append(0)

    return pd.DataFrame(data=data)


# helper function that takes a BeautifulSoup object and converts it into a pandas dataframe containing a WR/TE game log
def wr_game_log(soup: BeautifulSoup, season: int) -> pd.DataFrame:
    # Most relevant WR stats, in my opinion.
    # Could adjust if necessary (maybe figure out how to incorporate rushing stats?)

    data = {
        'date': [],
        'week': [],
        'team': [],
        'game_location': [],
        'opp': [],
        'result': [],
        'team_pts': [],
        'opp_pts': [],
        'tgt': [],
        'rec': [],
        'rec_yds': [],
        'rec_td': [],
        'snap_pct': [],
    }  # type: dict

    table_rows = soup.find('tbody').find_all('tr')

    # ignore inactive or DNP games
    to_ignore = []
    for i in range(len(table_rows)):
        elements = table_rows[i].find_all('td')
        x = elements[len(elements) - 1].text
        if x == 'Inactive' or x == 'Did Not Play' or x == 'Injured Reserve':
            to_ignore.append(i)

    # adding data to data dictionray
    for i in range(len(table_rows)):
        if i not in to_ignore:
            data['date'].append(table_rows[i].find('td', {'data-stat': 'game_date'}).text)
            data['week'].append(int(table_rows[i].find('td', {'data-stat': 'week_num'}).text))
            data['team'].append(table_rows[i].find('td', {'data-stat': 'team'}).text)
            data['game_location'].append(table_rows[i].find('td', {'data-stat': 'game_location'}).text)
            data['opp'].append(table_rows[i].find('td', {'data-stat': 'opp'}).text)
            data['result'].append(table_rows[i].find('td', {'data-stat': 'game_result'}).text.split(' ')[0])
            data['team_pts'].append(
                int(table_rows[i].find('td', {'data-stat': 'game_result'}).text.split(' ')[1].split('-')[0])
            )
            data['opp_pts'].append(
                int(table_rows[i].find('td', {'data-stat': 'game_result'}).text.split(' ')[1].split('-')[1])
            )
            data['tgt'].append(int(table_rows[i].find('td', {'data-stat': 'targets'}).text))
            data['rec'].append(int(table_rows[i].find('td', {'data-stat': 'rec'}).text))
            data['rec_yds'].append(int(table_rows[i].find('td', {'data-stat': 'rec_yds'}).text))
            data['rec_td'].append(int(table_rows[i].find('td', {'data-stat': 'rec_td'}).text))
            if season > 2011:
                data['snap_pct'].append(float(int(table_rows[i].find('td', {'data-stat': 'off_pct'}).text[:-1]) / 100))
            else:
                data['snap_pct'].append('Not Available')

    return pd.DataFrame(data=data)


def rb_game_log(soup: BeautifulSoup) -> pd.DataFrame:
    # Most relevant RB stats, in my opinion. Could adjust if necessary
    data = {
        'date': [],
        'week': [],
        'team': [],
        'game_location': [],
        'opp': [],
        'result': [],
        'team_pts': [],
        'opp_pts': [],
        'rush_att': [],
        'rush_yds': [],
        'rush_td': [],
        'tgt': [],
        'rec': [],
        'rec_yds': [],
        'rec_td': [],
    }  # type: dict

    table_rows = soup.find('tbody').find_all('tr')

    # ignore inactive or DNP games
    to_ignore = []
    for i in range(len(table_rows)):
        elements = table_rows[i].find_all('td')
        x = elements[len(elements) - 1].text
        if x == 'Inactive' or x == 'Did Not Play' or x == 'Injured Reserve':
            to_ignore.append(i)

    # adding data to data dictionary
    for i in range(len(table_rows)):
        if i not in to_ignore:
            data['date'].append(table_rows[i].find('td', {'data-stat': 'game_date'}).text)
            data['week'].append(int(table_rows[i].find('td', {'data-stat': 'week_num'}).text))
            data['team'].append(table_rows[i].find('td', {'data-stat': 'team'}).text)
            data['game_location'].append(table_rows[i].find('td', {'data-stat': 'game_location'}).text)
            data['opp'].append(table_rows[i].find('td', {'data-stat': 'opp'}).text)
            data['result'].append(table_rows[i].find('td', {'data-stat': 'game_result'}).text.split(' ')[0])
            data['team_pts'].append(
                int(table_rows[i].find('td', {'data-stat': 'game_result'}).text.split(' ')[1].split('-')[0])
            )
            data['opp_pts'].append(
                int(table_rows[i].find('td', {'data-stat': 'game_result'}).text.split(' ')[1].split('-')[1])
            )
            data['rush_att'].append(int(table_rows[i].find('td', {'data-stat': 'rush_att'}).text)) if table_rows[
                i
            ].find('td', {'data-stat': 'rush_att'}).text != '' else data['rush_att'].append(0)
            data['rush_yds'].append(int(table_rows[i].find('td', {'data-stat': 'rush_yds'}).text)) if table_rows[
                i
            ].find('td', {'data-stat': 'rush_yds'}).text != '' else data['rush_yds'].append(0)
            data['rush_td'].append(int(table_rows[i].find('td', {'data-stat': 'rush_td'}).text)) if table_rows[i].find(
                'td', {'data-stat': 'rush_td'}
            ).text != '' else data['rush_td'].append(0)
            data['tgt'].append(int(table_rows[i].find('td', {'data-stat': 'targets'}).text)) if table_rows[i].find(
                'td', {'data-stat': 'targets'}
            ).text != '' else data['tgt'].append(0)
            data['rec'].append(int(table_rows[i].find('td', {'data-stat': 'rec'}).text)) if table_rows[i].find(
                'td', {'data-stat': 'rec'}
            ).text != '' else data['rec'].append(0)
            data['rec_yds'].append(int(table_rows[i].find('td', {'data-stat': 'rec_yds'}).text)) if table_rows[i].find(
                'td', {'data-stat': 'rec_yds'}
            ).text != '' else data['rec_yds'].append(0)
            data['rec_td'].append(int(table_rows[i].find('td', {'data-stat': 'rec_td'}).text)) if table_rows[i].find(
                'td', {'data-stat': 'rec_td'}
            ).text != '' else data['rec_td'].append(0)

    return pd.DataFrame(data=data)


def main():
    print(get_player_game_log('Jonathan Taylor', 'RB', 2021))


if __name__ == '__main__':
    main()
