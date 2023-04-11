from pro_football_reference_web_scraper import player_splits as p
import pandas as pd


class TestClass:
    # UNIT TESTS ------------------------- #

    def test_format_game_log(self):
        # create a fake DataFrame
        fake_data = {'game_location': ['@', '', '@'], 'week': [1, 2, 3]}
        fake_df = pd.DataFrame(fake_data)

        # check that the week column is dropped
        # and game_location column is converted to home and away
        expected = pd.DataFrame({'game_location': ['away', 'home', 'away']})
        assert p.format_game_log(fake_df).equals(expected)

    def test_splits_averages(self):
        # create a fake DataFrame
        fake_data = {'team': ['A', 'A', 'B'], 'points': [100, 200, 300]}
        fake_df = pd.DataFrame(fake_data)

        # team A has an average of 150 points and played in 2 games
        result = p.splits_averages(fake_df, grouping='team')
        assert result['points']['A'] == 150
        assert result['games']['A'] == 2

    def test_splits_sum(self):
        # create a fake DataFrame
        fake_data = {'team': ['A', 'A', 'B'], 'points': [100, 200, 300]}
        fake_df = pd.DataFrame(fake_data)

        # team A has a total of 300 points and played in 2 games
        result = p.splits_sum(fake_df, grouping='team')
        assert result['points']['A'] == 300
        assert result['games']['A'] == 2
