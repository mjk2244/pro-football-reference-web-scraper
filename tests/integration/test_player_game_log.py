from src import player_game_log as p


class TestClass:
    # INTEGRATION TESTS
    def test_get_player_game_log(self):
        # Tom Brady had 4694 passing yards in 2022
        assert p.get_player_game_log("Tom Brady", 2022)['Pass_Yds'].sum() == 4694

        # Austin Ekeler had 13 rushing touchdowns in 2022
        assert p.get_player_game_log("Austin Ekeler", 2022)['Rush_TD'].sum() == 13

        # Stefon Diggs had 1429 receiving yards in 2022
        assert p.get_player_game_log("Stefon Diggs", 2022)['Rec_Yds'].sum() == 1429
