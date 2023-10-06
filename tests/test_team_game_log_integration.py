from pro_football_reference_web_scraper import team_game_log as t
import pytest
import time


class TestClass:
    # INTEGRATION TESTS
    def test_get_team_game_log(self):
        time.sleep(8)
        bills_game_log = t.get_team_game_log('Buffalo Bills', 2022)

        # the Bills only played 16 games in 2022 due to the cancellation of their Week 17 game
        assert len(bills_game_log.index) == 16

        # the Bills recorded 6361 total yards in 2022
        assert bills_game_log['tot_yds'].sum() == 6361

        w = 0
        for index, row in bills_game_log.iterrows():
            if row['result'] == 'W':
                w += 1
        # the Bills won 13 games in 2022
        assert w == 13

        # Team with blank cell data for week 17 (record 15) of 2003 regular season
        assert t.get_team_game_log('Oakland Raiders', 2003)['pass_yds'][15] == 0

        # misspelled team name
        with pytest.raises(Exception):
            t.get_team_game_log('Bufalo Bills', 2022)

        # invalid team-season combo
        with pytest.raises(Exception):
            t.get_team_game_log('Houston Texans', 2000)
