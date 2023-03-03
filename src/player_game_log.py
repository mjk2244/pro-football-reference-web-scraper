import pandas as pd  # type: ignore
from bs4 import BeautifulSoup
import requests


# function that returns a player's game log in a given season
def get_player_game_log(player="Tom Brady", season=2022) -> pd.DataFrame:
    # make HTTP request and extract HTML
    r = make_request(player, season)

    # parse HTML using BeautifulSoup
    soup = get_soup(r)

    # checking the player's position
    position = str(soup.find_all('p')[1])

    # generating the appropriate game log format according to position
    if "QB" in position:
        return qb_game_log(soup)
    elif "WR" in position or "TE" in position:
        return wr_game_log(soup)
    elif "RB" in position:
        return rb_game_log(soup)


# helper function that makes a HTTP request
def make_request(player="Tom Brady", season=2022):
    # NOTE: the following scheme won't work for all players
    # e.g. Josh Allen's game log can be found at https://www.pro-football-reference.com/players/A/AlleJo02/gamelog/2022/
    # An older player named Josh Allen is AlleJo00 and an older player named Jonathan Allen is AllJo01
    # A potential solution is to go to https://www.pro-football-reference.com/players/A/ and retrieve the href for the
    # correct Josh Allen, which may require the player's position
    # Similar issues exist for numerous other players,
    # e.g. Damien Harris: https://www.pro-football-reference.com/players/H/HarrDa06/gamelog/2022/advanced/

    # TODO: Fix the problem described above

    name_split = player.split(" ")
    last_initial = name_split[1][0]
    lname_first_four = name_split[1][0:4]
    fname_first_two = name_split[0][0:2]
    url = "https://pro-football-reference.com/players/%s/%s%s00/gamelog/%s/" % (
        last_initial,
        lname_first_four,
        fname_first_two,
        str(season),
    )
    return requests.get(url)


# helper function that takes a requests.Response object and returns a BeautifulSoup object
def get_soup(request):
    return BeautifulSoup(request.text, "html.parser")


# helper function that takes a BeautifulSoup object and converts it into a pandas dataframe containing a QB game log
def qb_game_log(soup: BeautifulSoup) -> pd.DataFrame:
    # TODO: account for players who did missed game(s)
    # e.g. Jimmy Garoppolo starting in week 13: https://www.pro-football-reference.com/players/G/GaroJi00/gamelog/2022/

    # Most relevant QB stats, in my opinion. Could adjust if necessary
    data = {
        "Date": [],
        "Week": [],
        "Team": [],
        "Game_Location": [],
        "Opp": [],
        "Result": [],
        "Cmp": [],
        "Att": [],
        "Pass_Yds": [],
        "Pass_TD": [],
        "Int": [],
        "Rating": [],
        "Sacked": [],
        "Rush_Att": [],
        "Rush_Yds": [],
        "Rush_TD": [],
    }  # type: dict

    table_rows = soup.find('tbody').find_all('tr')
    # adding data to data dictionary
    for row in table_rows:
        data["Date"].append(row.find('td', {'data-stat': 'game_date'}).text)
        data["Week"].append(int(row.find('td', {'data-stat': 'week_num'}).text))
        data["Team"].append(row.find('td', {'data-stat': 'team'}).text)
        data["Game_Location"].append(row.find('td', {'data-stat': 'game_location'}).text)
        data["Opp"].append(row.find('td', {'data-stat': 'opp'}).text)
        data["Result"].append(row.find('td', {'data-stat': 'game_result'}).text)
        data["Cmp"].append(int(row.find('td', {'data-stat': 'pass_cmp'}).text))
        data["Att"].append(int(row.find('td', {'data-stat': 'pass_att'}).text))
        data["Pass_Yds"].append(int(row.find('td', {'data-stat': 'pass_yds'}).text))
        data["Pass_TD"].append(int(row.find('td', {'data-stat': 'pass_td'}).text))
        data["Int"].append(int(row.find('td', {'data-stat': 'pass_int'}).text))
        data["Rating"].append(float(row.find('td', {'data-stat': 'pass_rating'}).text))
        data["Sacked"].append(int(row.find('td', {'data-stat': 'pass_sacked'}).text))
        data["Rush_Att"].append(int(row.find('td', {'data-stat': 'rush_att'}).text))
        data["Rush_Yds"].append(int(row.find('td', {'data-stat': 'rush_yds'}).text))
        data["Rush_TD"].append(int(row.find('td', {'data-stat': 'rush_td'}).text))

    print(pd.DataFrame(data=data))
    return pd.DataFrame(data=data)


# helper function that takes a BeautifulSoup object and converts it into a pandas dataframe containing a WR/TE game log
def wr_game_log(soup: BeautifulSoup) -> pd.DataFrame:
    # TODO: account for players who did missed game(s)
    # e.g. Cooper Kupp starting in week 10: https://www.pro-football-reference.com/players/K/KuppCo00/gamelog/2022/

    # Most relevant WR stats, in my opinion.
    # Could adjust if necessary (maybe figure out how to incorporate rushing stats?)
    data = {
        "Date": [],
        "Week": [],
        "Team": [],
        "Game_Location": [],
        "Opp": [],
        "Result": [],
        "Tgt": [],
        "Rec": [],
        "Rec_Yds": [],
        "Rec_TD": [],
        "Snap_Pct": [],
    }  # type: dict

    table_rows = soup.find('tbody').find_all('tr')
    # adding data to data dictionray
    for row in table_rows:
        data["Date"].append(row.find('td', {'data-stat': 'game_date'}).text)
        data["Week"].append(int(row.find('td', {'data-stat': 'week_num'}).text))
        data["Team"].append(row.find('td', {'data-stat': 'team'}).text)
        data["Game_Location"].append(row.find('td', {'data-stat': 'game_location'}).text)
        data["Opp"].append(row.find('td', {'data-stat': 'opp'}).text)
        data["Result"].append(row.find('td', {'data-stat': 'game_result'}).text)
        data["Tgt"].append(int(row.find('td', {'data-stat': 'targets'}).text))
        data["Rec"].append(int(row.find('td', {'data-stat': 'rec'}).text))
        data["Rec_Yds"].append(int(row.find('td', {'data-stat': 'rec_yds'}).text))
        data["Rec_TD"].append(int(row.find('td', {'data-stat': 'rec_td'}).text))
        data["Snap_Pct"].append(float(int(row.find('td', {'data-stat': 'off_pct'}).text[:-1]) / 100))

    print(pd.DataFrame(data=data))
    return pd.DataFrame(data=data)


def rb_game_log(soup: BeautifulSoup) -> pd.DataFrame:
    # TODO: account for players who did missed game(s)
    # e.g. Saquon Barkley in week 18: https://www.pro-football-reference.com/players/B/BarkSa00/gamelog/2022/

    # Most relevant RB stats, in my opinion. Could adjust if necessary
    data = {
        "Date": [],
        "Week": [],
        "Team": [],
        "Game_Location": [],
        "Opp": [],
        "Result": [],
        "Rush_Att": [],
        "Rush_Yds": [],
        "Rush_TD": [],
        "Tgt": [],
        "Rec_Yds": [],
        "Rec_TD": [],
    }  # type: dict

    table_rows = soup.find('tbody').find_all('tr')

    # adding data to dictionary
    for row in table_rows:
        data["Date"].append(row.find('td', {'data-stat': 'game_date'}).text)
        data["Week"].append(int(row.find('td', {'data-stat': 'week_num'}).text))
        data["Team"].append(row.find('td', {'data-stat': 'team'}).text)
        data["Game_Location"].append(row.find('td', {'data-stat': 'game_location'}).text)
        data["Opp"].append(row.find('td', {'data-stat': 'opp'}).text)
        data["Result"].append(row.find('td', {'data-stat': 'game_result'}).text)
        data["Rush_Att"].append(int(row.find('td', {'data-stat': 'rush_att'}).text))
        data["Rush_Yds"].append(int(row.find('td', {'data-stat': 'rush_yds'}).text))
        data["Rush_TD"].append(int(row.find('td', {'data-stat': 'rush_td'}).text))
        data["Tgt"].append(int(row.find('td', {'data-stat': 'targets'}).text))
        data["Rec_Yds"].append(int(row.find('td', {'data-stat': 'rec_yds'}).text))
        data["Rec_TD"].append(int(row.find('td', {'data-stat': 'rec_td'}).text))

    print(pd.DataFrame(data=data))
    return pd.DataFrame(data=data)


def main():
    get_player_game_log(player="Stefon Diggs", season=2022)


if __name__ == "__main__":
    main()
