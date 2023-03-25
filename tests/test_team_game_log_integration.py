from pro_football_reference_web_scraper import team_game_log as t


class TestClass:
    # INTEGRATION TESTS
    def test_get_team_game_log(self):
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
