from src import player_game_log as p
import requests
from bs4 import BeautifulSoup
import pytest

class TestClass:
    # UNIT TESTS ------------------------- #

    def test_make_request(self):
        response = p.make_request("Tom Brady", 2022)
        assert response.status_code == 200

    def test_get_soup(self):
        url = "https://www.pro-football-reference.com/players/B/BradTo00/gamelog/2022/"
        response = requests.get(url)
        soup = p.get_soup(response)
        assert soup.find('h1').find('span').text == "Tom Brady"

    def test_qb_game_log(self):
        # making request and BeautifulSoup for Tom Brady's game log
        url = "https://www.pro-football-reference.com/players/B/BradTo00/gamelog/2022/"
        response = requests.get(url)
        soup = p.get_soup(response)
        df = p.qb_game_log(soup)

        # Tom Brady had 4694 passing yards in 2022
        assert df['Pass_Yds'].sum() == 4694

    def test_rb_game_log(self):
        # making request and BeautifulSoup Austin Ekeler's game log
        url = "https://www.pro-football-reference.com/players/E/EkelAu00/gamelog/2022/"
        response = requests.get(url)
        soup = p.get_soup(response)
        df = p.rb_game_log(soup)

        # Austin Ekeler had 915 rush yards in 2022
        assert df['Rush_Yds'].sum() == 915

    def test_wr_game_log(self):
        # making request and BeautifulSoup for Stefon Diggs' game log
        url = "https://www.pro-football-reference.com/players/D/DiggSt00/gamelog/2022/"
        response = requests.get(url)
        soup = p.get_soup(response)
        df = p.rb_game_log(soup)

        # Stefon Diggs had 1429 receiving yards in 2022
        assert df['Rec_Yds'].sum() == 1429

    def test_get_player_game_log(self):
        # Tom Brady threw 25 touchdowns in 2022
        assert p.get_player_game_log("Tom Brady", 2022)['Pass_TD'].sum() == 25
        # Austin Ekeler rushed for 13 touchdowns in 2022
        assert p.get_player_game_log("Austin Ekeler", 2022)['Rush_TD'].sum() == 13
        # Stefon Diggs had 11 receiving touchdowns in 2022
        assert p.get_player_game_log("Stefon Diggs", 2022)['Rec_TD'].sum() == 11