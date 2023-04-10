from pro_football_reference_web_scraper import player_splits as p
import time


class TestClass:
    # INTEGRATION TESTS

    def test_home_road(self):
        time.sleep(3)
        player = 'Davante Adams'
        position = 'WR'
        season = 2022
        # Davante Adams had 8 TDs in road games and 6 TDs in home games in 2022
        assert p.home_road(player, position, season, avg=False)['rec_td'][0] == 8
        assert p.home_road(player, position, season, avg=False)['rec_td'][1] == 6

        # Davante Adams averaged 6.5 receptions/game in home games in 2022
        assert p.home_road(player, position, season, avg=True)['rec'][1] == 6.5

    def test_win_loss(self):
        player = 'Justin Herbert'
        position = 'QB'
        season = 2022
        # Justin Herbert averaged 40.6 pass attempts in wins in 2022
        assert p.win_loss(player, position, season, avg=True)['pass_att'][1] == 40.6

        # Justin Herbert threw for 12 touchdowns in losses in 2022
        assert p.win_loss(player, position, season, avg=False)['pass_td'][0] == 12
