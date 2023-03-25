from pro_football_reference_web_scraper import player_game_log as p
from bs4 import BeautifulSoup
from unittest.mock import MagicMock, patch
import pandas as pd


class TestClass:
    # UNIT TESTS ------------------------- #

    def test_make_request_list(self):
        response = p.make_request_list('Ryan Tannehill', 'QB', 2022)
        # asserting that the HTTP request was made with the correct url
        assert response.url == 'https://www.pro-football-reference.com/players/T/'

    def test_get_href(self):
        fake_html = """<div id = 'div_players'><p><a href="/players/A/AlleJo00.htm">Josh Allen</a> (C) 2014-2014</p>
        <p><b><a href="/players/A/AlleJo02.htm">Josh Allen</a> (QB)</b> 2018-2022</p>
        <p><b><a href="/players/A/AlleJo03.htm">Josh Allen</a> (EDGE)</b> 2019-2022</p></div>"""
        soup = BeautifulSoup(fake_html, 'html.parser')
        assert p.get_href('Josh Allen', 'C', 2014, soup) == '/players/A/AlleJo00.htm'
        assert p.get_href('Josh Allen', 'QB', 2022, soup) == '/players/A/AlleJo02.htm'
        assert p.get_href('Josh Allen', 'EDGE', 2020, soup) == '/players/A/AlleJo03.htm'

    def test_make_request_player(self):
        response = p.make_request_player('/players/G/GurlTo01', 2018)
        # asserting that the "HTTP request was made with the correct url"
        assert response.url == 'https://www.pro-football-reference.com/players/G/GurlTo01/gamelog/2018/'

    @patch('requests.get')
    def test_get_soup(self, mock_requests):
        # mocking HTTP response
        mock_response = MagicMock()
        mock_response.text = "<!DOCTYPE html>\n"
        soup = p.get_soup(mock_response)
        # asserting that the soup text and mock response text are the same
        assert mock_response.text == soup.prettify()

    def test_qb_game_log(self):
        # fake HTML to create BeautifulSoup object
        fake_html = """<tbody><tr><td data-stat='game_date'>2022-09-11</td><td data-stat='week_num'>1</td>
        <td data-stat='team'>TAM</td><td data-stat='game_location'>@</td><td data-stat='opp'>DAL</td>
        <td data-stat='game_result'>W 19-3</td><td data-stat='pass_cmp'>18</td><td data-stat='pass_att'>27</td>
        <td data-stat='pass_yds'>212</td><td data-stat='pass_td'>1</td><td data-stat='pass_int'>1</td>
        <td data-stat='pass_rating'>87.3</td><td data-stat='pass_sacked'>2</td><td data-stat='rush_att'>1</td>
        <td data-stat='rush_yds'>1</td><td data-stat='rush_td'>1</td></tr></tbody>"""
        soup = BeautifulSoup(fake_html, "html.parser")

        # fake dataframe to check with returned dataframe
        fake_df = pd.DataFrame(
            {
                "Date": ["2022-09-11"],
                "Week": [1],
                "Team": ["TAM"],
                "Game_Location": ["@"],
                "Opp": ["DAL"],
                "Result": ["W 19-3"],
                "Cmp": [18],
                "Att": [27],
                "Pass_Yds": [212],
                "Pass_TD": [1],
                "Int": [1],
                "Rating": [87.3],
                "Sacked": [2],
                "Rush_Att": [1],
                "Rush_Yds": [1],
                "Rush_TD": [1],
            }
        )
        # asserting that the returned dataframe is expected

        assert p.qb_game_log(soup).equals(fake_df)

    def test_rb_game_log(self):
        # fake HTML to create BeautifulSoup object
        fake_html = """<tbody><tr><td data-stat='game_date'>2022-09-11</td><td data-stat='week_num'>1</td>
        <td data-stat='team'>TAM</td><td data-stat='game_location'>@</td><td data-stat='opp'>DAL</td>
        <td data-stat='game_result'>W 19-3</td><td data-stat='rush_att'>18</td><td data-stat='rush_yds'>27</td>
        <td data-stat='rush_td'>212</td><td data-stat='targets'>1</td><td data-stat='rec_yds'>1</td>
        <td data-stat='rec_td'>1</td></tr></tbody>"""
        soup = BeautifulSoup(fake_html, "html.parser")

        # fake dataframe to check with returned dataframe
        fake_df = pd.DataFrame(
            {
                "Date": ["2022-09-11"],
                "Week": [1],
                "Team": ["TAM"],
                "Game_Location": ["@"],
                "Opp": ["DAL"],
                "Result": ["W 19-3"],
                "Rush_Att": [18],
                "Rush_Yds": [27],
                "Rush_TD": [212],
                "Tgt": [1],
                "Rec_Yds": [1],
                "Rec_TD": [1],
            }
        )

        # asserting that the returned dataframe is expected
        assert p.rb_game_log(soup).equals(fake_df)

    def test_wr_game_log(self):
        # fake HTML to create BeautifulSoup object
        fake_html = """<tbody><tr><td data-stat='game_date'>2022-09-11</td><td data-stat='week_num'>1</td>
        <td data-stat='team'>TAM</td><td data-stat='game_location'>@</td><td data-stat='opp'>DAL</td>
        <td data-stat='game_result'>W 19-3</td><td data-stat='targets'>18</td><td data-stat='rec'>27</td>
        <td data-stat='rec_yds'>212</td><td data-stat='rec_td'>1</td><td data-stat='rec_yds'>1</td>
        <td data-stat='off_pct'>87%</td></tr></tbody>"""
        soup = BeautifulSoup(fake_html, "html.parser")

        # fake dataframe to check with returned dataframe
        fake_df = pd.DataFrame(
            {
                "Date": ["2022-09-11"],
                "Week": [1],
                "Team": ["TAM"],
                "Game_Location": ["@"],
                "Opp": ["DAL"],
                "Result": ["W 19-3"],
                "Tgt": [18],
                "Rec": [27],
                "Rec_Yds": [212],
                "Rec_TD": [1],
                "Snap_Pct": [0.87],
            }
        )

        # asserting that the returned dataframe is expected
        assert p.wr_game_log(soup).equals(fake_df)
