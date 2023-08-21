from pro_football_reference_web_scraper import team_splits as t
import time


class TestClass:
    # INTEGRATION TESTS

    def test_home_road(self):
        time.sleep(5)
        team = 'Chicago Bears'
        season = 2022

        splits = t.home_road(team, season, avg=True)
        # the Bears went 2-7 at home in 2022
        assert splits['wins']['home'] == 2 and splits['losses']['home'] == 7

        # the Bears scored 176 points in home games in 2022
        assert t.home_road(team, season, avg=False)['points_for']['home'] == 176

    def test_win_loss(self):
        team = 'Philadelphia Eagles'
        season = 2021
        # the Eagles scored 20.375 points per losses in 2021
        assert t.win_loss(team, season, avg=True)['points_for']['L'] == 20.375

        # the Eagles scored 274 points in wins in 2021
        assert t.win_loss(team, season, avg=False)['points_for']['W'] == 281
