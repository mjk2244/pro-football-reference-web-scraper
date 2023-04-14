from pro_football_reference_web_scraper import team_game_log as t
import pandas as pd


def home_road(team: str, season: int, avg=True) -> pd.DataFrame:
    """A function that returns a team's home-road splits in a given season

    Returns a pandas DataFrame of a team's stats at home vs. on the road

    Args:
        team (str): A NFL team's name, as it appears on Pro Football Reference
        season (int): The season of the stats you are trying to retrieve
        avg (bool): Whether you want the stats as averages or sums (default = True)

    Returns:
        pandas.DataFrame: A pandas DataFrame of a team's home-road splits

    """

    game_log = t.get_team_game_log(team, season)
    game_log = format_game_log(game_log)  # get rid of extraneous stats

    if avg:
        return splits_averages(game_log, 'game_location')

    else:
        return splits_sum(game_log, 'game_location')


def win_loss(team: str, season: int, avg=True) -> pd.DataFrame:
    """A function that returns a team's win-loss splits in a given season

    Returns a pandas DataFrame of a player's stats in wins vs. in losses

    Args:
        team (str): A NFL team's name, as it appears on Pro Football Reference
        season (int): The season of the stats you are trying to retrieve
        avg (bool): Whether you want the stats as averages or sums (default = True)

    Returns:
        pandas.DataFrame: A pandas DataFrame of a team's win-loss splits

    """

    game_log = t.get_team_game_log(team, season)
    game_log = format_game_log(game_log)  # get rid of extraneous stats

    if avg:
        return splits_averages(game_log, 'result')

    else:
        return splits_sum(game_log, 'result')


# helper function to format game log for grouping
def format_game_log(game_log: pd.DataFrame) -> pd.DataFrame:
    game_log['home_team'] = game_log['home_team'].replace(True, 'home')
    game_log['home_team'] = game_log['home_team'].replace(False, 'away')
    game_log.rename(columns={'home_team': 'game_location'}, inplace=True)
    game_log = game_log.drop(['week', 'day', 'rest_days', 'distance_travelled', 'opp'], axis=1)
    return game_log


# helper function to group a game log and return its averages
def splits_averages(game_log: pd.DataFrame, grouping: str) -> pd.DataFrame:
    # count # of games for each grouping
    counts = game_log.groupby(grouping).size().to_frame('games')

    # count # of wins and losses for each grouping (if home-road)
    if grouping == 'game_location':
        home_wins = 0
        home_losses = 0
        home_ties = 0
        road_wins = 0
        road_losses = 0
        road_ties = 0
        for ind in game_log.index:
            if game_log['game_location'][ind] == 'home':
                if game_log['result'][ind] == 'W':
                    home_wins += 1
                elif game_log['result'][ind] == 'L':
                    home_losses += 1
                else:
                    home_ties += 1
            if game_log['game_location'][ind] == 'away':
                if game_log['result'][ind] == 'W':
                    road_wins += 1
                elif game_log['result'][ind] == 'L':
                    road_losses += 1
                else:
                    road_ties += 1

    game_log = game_log.groupby(grouping).mean(numeric_only=True)
    if grouping == 'game_location':
        game_log.insert(0, 'wins', [road_wins, home_wins])
        game_log.insert(1, 'losses', [road_losses, home_losses])
        game_log.insert(1, 'ties', [road_ties, home_ties])
    game_log.insert(0, 'games', counts['games'])

    return game_log.iloc[::-1]


# helper function to group a game log and return its sums
def splits_sum(game_log: pd.DataFrame, grouping: str) -> pd.DataFrame:
    # count # of games for each grouping
    counts = game_log.groupby(grouping).size().to_frame('games')

    # count # of wins and losses for each grouping (if home-road)
    if grouping == 'game_location':
        home_wins = 0
        home_losses = 0
        home_ties = 0
        road_wins = 0
        road_losses = 0
        road_ties = 0
        for ind in game_log.index:
            if game_log['game_location'][ind] == 'home':
                if game_log['result'][ind] == 'W':
                    home_wins += 1
                elif game_log['result'][ind] == 'L':
                    home_losses += 1
                else:
                    home_ties += 1
            if game_log['game_location'][ind] == 'away':
                if game_log['result'][ind] == 'W':
                    road_wins += 1
                elif game_log['result'][ind] == 'L':
                    road_losses += 1
                else:
                    road_ties += 1

    game_log = game_log.groupby(grouping).sum(numeric_only=True)
    if grouping == 'game_location':
        game_log.insert(0, 'wins', [road_wins, home_wins])
        game_log.insert(1, 'losses', [road_losses, home_losses])
        game_log.insert(1, 'ties', [road_ties, home_ties])
    game_log.insert(0, 'games', counts['games'])

    return game_log.iloc[::-1]
