from pro_football_reference_web_scraper import player_game_log as p
import pandas as pd


def home_road(player: str, position: str, season: int, avg=True) -> pd.DataFrame:
    """A function that returns a player's home-road splits in a given season

    Returns a pandas DataFrame of a player's stats at home vs. on the road

    Args:
        player (str): A NFL player's full name, as it appears on Pro Football Reference
        position (str): The position the player plays. Must be 'QB', 'RB', 'WR', or 'TE'
        season (int): The season of the stats you are trying to retrieve
        avg (bool): Whether you want the stats as averages or sums (default = True)

    Returns:
        pandas.DataFrame: A pandas DataFrame of a player's home-road splits

    """

    game_log = p.get_player_game_log(player, position, season)
    game_log = format_game_log(game_log)  # get rid of extraneous stats

    if avg:
        return splits_averages(game_log, 'game_location')

    else:
        # doesn't make sense to sum snap pct
        if position == 'WR' or position == 'TE':
            game_log = game_log.drop('snap_pct', axis=1)
        return splits_sum(game_log, 'game_location')


def win_loss(player: str, position: str, season: int, avg=True) -> pd.DataFrame:
    """A function that returns a player's win-loss splits in a given season

    Returns a pandas DataFrame of a player's stats in wins vs. in losses

    Args:
        player (str): A NFL player's full name, as it appears on Pro Football Reference
        position (str): The position the player plays. Must be 'QB', 'RB', 'WR', or 'TE'
        season (int): The season of the stats you are trying to retrieve
        avg (bool): Whether you want the stats as averages or sums

    Returns:
        pandas.DataFrame: A pandas DataFrame of a player's win-loss splits

    """

    game_log = p.get_player_game_log(player, position, season)
    game_log = format_game_log(game_log)

    if avg:
        return splits_averages(game_log, 'result')

    else:
        # doesn't make sense to sum snap pct
        if position == 'WR' or position == 'TE':
            game_log = game_log.drop('snap_pct', axis=1)
        return splits_sum(game_log, 'result')


# helper function to properly format game log for grouping
def format_game_log(game_log: pd.DataFrame) -> pd.DataFrame:
    game_log['game_location'] = game_log['game_location'].replace('', 'home')
    game_log['game_location'] = game_log['game_location'].replace('@', 'away')
    game_log = game_log.drop('week', axis=1)
    return game_log


# helper function to group a game log and return its averages
def splits_averages(game_log: pd.DataFrame, grouping: str):
    # count number of games for each split
    counts = game_log.groupby(grouping).size().to_frame('games')
    game_log = game_log.groupby(grouping).mean(numeric_only=True)
    game_log.insert(0, 'games', counts['games'])
    return game_log.iloc[::-1]


def splits_sum(game_log: pd.DataFrame, grouping: str):
    # count number of games for each split
    counts = game_log.groupby(grouping).size().to_frame('games')
    game_log = game_log.groupby(grouping).sum(numeric_only=True)
    game_log.insert(0, 'games', counts['games'])
    return game_log.iloc[::-1]
