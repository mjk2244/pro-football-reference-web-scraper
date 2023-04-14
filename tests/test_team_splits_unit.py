from pro_football_reference_web_scraper import team_splits as p
import pandas as pd


class TestClass:
    # UNIT TESTS ------------------------- #

    def test_format_game_log(self):
        # create a fake DataFrame
        fake_data = {
            'week': [1, 2, 3],
            'day': [3, 4, 5],
            'rest_days': [5, 6, 7],
            'distance_travelled': [8, 9, 10],
            'opp': ['A', 'B', 'C'],
            'home_team': [True, False, True],
        }
        fake_df = pd.DataFrame(fake_data)
        print(fake_df)

        # check that the proper columns are dropped
        # home_team values are properly changed
        # and home_team is renamed to game_location
        expected = pd.DataFrame({'game_location': ['home', 'away', 'home']})
        assert p.format_game_log(fake_df).equals(expected)

    def test_splits_averages(self):
        # create a fake DataFrame
        fake_data = {
            'game_location': ['home', 'home', 'away'],
            'points_for': [10, 12, 14],
            'points_allowed': [15, 20, 25],
            'result': ['W', 'L', 'T'],
        }
        fake_df = pd.DataFrame(fake_data)
        result = p.splits_averages(fake_df, grouping='game_location')

        # 1 home win, 1 home loss, 0 home ties
        assert result['wins']['home'] == 1 and result['losses']['home'] == 1 and result['ties']['home'] == 0
        # 0 road wins, 0 road losses, 1 road tie
        assert result['wins']['away'] == 0 and result['losses']['away'] == 0 and result['ties']['away'] == 1

        # averaging 11 points_for at home, 14 on the road
        assert result['points_for']['home'] == 11 and result['points_for']['away'] == 14

        # averaging 17.5 points_allowed at home, 25 on the road
        assert result['points_allowed']['home'] == 17.5 and result['points_allowed']['away'] == 25

    def test_splits_sum(self):
        # create a fake DataFrame
        fake_data = {
            'game_location': ['home', 'home', 'away'],
            'points_for': [10, 12, 14],
            'points_allowed': [15, 20, 25],
            'result': ['W', 'L', 'T'],
        }
        fake_df = pd.DataFrame(fake_data)
        result = p.splits_sum(fake_df, grouping='game_location')

        # 1 home win, 1 home loss, 0 home ties
        assert result['wins']['home'] == 1 and result['losses']['home'] == 1 and result['ties']['home'] == 0
        # 0 road wins, 0 road losses, 1 road tie
        assert result['wins']['away'] == 0 and result['losses']['away'] == 0 and result['ties']['away'] == 1

        # 22 total points at home, 14 on road
        assert result['points_for']['home'] == 22 and result['points_for']['away'] == 14

        # 35 total points_allowed at home, 25 on the road
        assert result['points_allowed']['home'] == 35 and result['points_allowed']['away'] == 25
