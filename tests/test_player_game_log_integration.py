import pytest
from pro_football_reference_web_scraper import player_game_log as p
import time


class TestClass:
    # INTEGRATION TESTS
    def test_get_player_game_log(self):
        time.sleep(5)
        # Tom Brady had 4694 passing yards in 2022
        assert p.get_player_game_log('Tom Brady', 'QB', 2022)['pass_yds'].sum() == 4694

        # Austin Ekeler had 13 rushing touchdowns in 2022
        assert p.get_player_game_log('Austin Ekeler', 'RB', 2022)['rush_td'].sum() == 13

        # Stefon Diggs had 1429 receiving yards in 2022
        assert p.get_player_game_log('Stefon Diggs', 'WR', 2022)['rec_yds'].sum() == 1429

        # Wide Receivers did not have snap pct before 2012
        assert p.get_player_game_log('Antonio Brown', 'WR', 2011)['snap_pct'][0] == 'Not Available'

        # Tight ends did not have snap pct before 2012
        assert p.get_player_game_log('Antonio Gates', 'TE', 2010)['snap_pct'][0] == 'Not Available'

        # Quarterback with blank cell data for week 3 (record 1, ignoring 2 'Did Not Play' weeks) of 2023 regular season
        assert p.get_player_game_log('Dorian Thompson-Robinson', 'QB', 2023)['cmp'][0] == 0

        # Running back with blank cell data for week 17 (record 9, ignoring 7 'DNP' weeks) of 2022 regular season
        assert p.get_player_game_log('Kyren Williams', 'RB', 2022)['rush_yds'][9] == 0

        # improper position formatting
        with pytest.raises(Exception):
            p.get_player_game_log('Patrick Mahomes', 'Quarterback', 2022)

        # player with wrong position
        with pytest.raises(Exception):
            p.get_player_game_log('Patrick Mahomes', 'RB', 2022)

        # player in wrong season
        with pytest.raises(Exception):
            p.get_player_game_log('Patrick Mahomes', 'QB', 2016)
