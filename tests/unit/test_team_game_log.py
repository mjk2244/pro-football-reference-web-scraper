from pro_football_reference_web_scraper import team_game_log as t
from bs4 import BeautifulSoup
from unittest.mock import MagicMock, patch


class TestClass:
    # UNIT TESTS ------------------------- #

    def test_make_request(self):
        response = t.make_request('Kansas City Chiefs', 2022)
        # asserting that the HTTP request was made with the correct url
        assert response.url == 'https://www.pro-football-reference.com/teams/kan/2022.htm'

    @patch('requests.get')
    def test_get_soup(self, mock_requests):
        # mocking HTTP response
        mock_response = MagicMock()
        mock_response.text = "<!DOCTYPE html>\n"
        soup = t.get_soup(mock_response)
        # asserting that the soup text and mock response text are the same
        assert mock_response.text == soup.prettify()

    def test_collect_data(self):
        # HTML from Kansas City Chiefs 2022 season to create BeautifulSoup object
        fake_html = """<tbody></table>
        <tbody>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2022-09-11" >September 11</td>
        <td class="right " data-stat="game_time" csk="16.25" >4:25PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202209110crd.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >1-0</td><td class="right " data-stat="game_location" >@</td>
        <td class="left " data-stat="opp" ><a href="/teams/crd/2022.htm">Arizona Cardinals</a></td>
        <td class="right " data-stat="pts_off" >44</td><td class="right " data-stat="pts_def" >21</td>
        <td class="right " data-stat="first_down_off" >33</td><td class="right " data-stat="yards_off" >488</td>
        <td class="right " data-stat="pass_yds_off" >360</td><td class="right " data-stat="rush_yds_off" >128</td>
        <td class="right " data-stat="to_off" >1</td><td class="right " data-stat="first_down_def" >18</td>
        <td class="right " data-stat="yards_def" >282</td><td class="right " data-stat="pass_yds_def" >179</td>
        <td class="right " data-stat="rush_yds_def" >103</td><td class="right iz" data-stat="to_def" ></td>
        <td class="right " data-stat="exp_pts_off" >33.41</td><td class="right " data-stat="exp_pts_def" >-2.29</td>
        <td class="right " data-stat="exp_pts_st" >-6.88</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th>
        <td class="left " data-stat="game_day_of_week" >Thu</td>
        <td class="left " data-stat="game_date" csk="2022-09-15" >September 15</td>
        <td class="right " data-stat="game_time" csk="20.15" >8:15PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202209150kan.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >2-0</td><td class="right iz" data-stat="game_location" ></td>
        <td class="left " data-stat="opp" ><a href="/teams/sdg/2022.htm">Los Angeles Chargers</a></td>
        <td class="right " data-stat="pts_off" >27</td><td class="right " data-stat="pts_def" >24</td>
        <td class="right " data-stat="first_down_off" >15</td><td class="right " data-stat="yards_off" >319</td>
        <td class="right " data-stat="pass_yds_off" >226</td><td class="right " data-stat="rush_yds_off" >93</td>
        <td class="right iz" data-stat="to_off" ></td><td class="right " data-stat="first_down_def" >21</td>
        <td class="right " data-stat="yards_def" >401</td><td class="right " data-stat="pass_yds_def" >326</td>
        <td class="right " data-stat="rush_yds_def" >75</td><td class="right " data-stat="to_def" >1</td>
        <td class="right " data-stat="exp_pts_off" >5.54</td><td class="right " data-stat="exp_pts_def" >-4.12</td>
        <td class="right " data-stat="exp_pts_st" >3.72</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2022-09-25" >September 25</td>
        <td class="right " data-stat="game_time" csk="13.00" >1:00PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202209250clt.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >L</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >2-1</td><td class="right " data-stat="game_location" >@</td>
        <td class="left " data-stat="opp" ><a href="/teams/clt/2022.htm">Indianapolis Colts</a></td>
        <td class="right " data-stat="pts_off" >17</td><td class="right " data-stat="pts_def" >20</td>
        <td class="right " data-stat="first_down_off" >20</td><td class="right " data-stat="yards_off" >315</td>
        <td class="right " data-stat="pass_yds_off" >257</td><td class="right " data-stat="rush_yds_off" >58</td>
        <td class="right " data-stat="to_off" >2</td><td class="right " data-stat="first_down_def" >19</td>
        <td class="right " data-stat="yards_def" >259</td><td class="right " data-stat="pass_yds_def" >177</td>
        <td class="right " data-stat="rush_yds_def" >82</td><td class="right " data-stat="to_def" >1</td>
        <td class="right " data-stat="exp_pts_off" >1.78</td><td class="right " data-stat="exp_pts_def" >7.10</td>
        <td class="right " data-stat="exp_pts_st" >-13.31</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2022-10-02" >October 2</td>
        <td class="right " data-stat="game_time" csk="20.20" >8:20PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202210020tam.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >3-1</td><td class="right " data-stat="game_location" >@</td>
        <td class="left " data-stat="opp" ><a href="/teams/tam/2022.htm">Tampa Bay Buccaneers</a></td>
        <td class="right " data-stat="pts_off" >41</td><td class="right " data-stat="pts_def" >31</td>
        <td class="right " data-stat="first_down_off" >27</td><td class="right " data-stat="yards_off" >417</td>
        <td class="right " data-stat="pass_yds_off" >228</td><td class="right " data-stat="rush_yds_off" >189</td>
        <td class="right " data-stat="to_off" >1</td><td class="right " data-stat="first_down_def" >27</td>
        <td class="right " data-stat="yards_def" >376</td><td class="right " data-stat="pass_yds_def" >373</td>
        <td class="right " data-stat="rush_yds_def" >3</td><td class="right " data-stat="to_def" >2</td>
        <td class="right " data-stat="exp_pts_off" >17.12</td><td class="right " data-stat="exp_pts_def" >-14.15</td>
        <td class="right " data-stat="exp_pts_st" >5.33</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th>
        <td class="left " data-stat="game_day_of_week" >Mon</td>
        <td class="left " data-stat="game_date" csk="2022-10-10" >October 10</td>
        <td class="right " data-stat="game_time" csk="20.15" >8:15PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202210100kan.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >4-1</td><td class="right iz" data-stat="game_location" ></td>
        <td class="left " data-stat="opp" ><a href="/teams/rai/2022.htm">Las Vegas Raiders</a></td>
        <td class="right " data-stat="pts_off" >30</td><td class="right " data-stat="pts_def" >29</td>
        <td class="right " data-stat="first_down_off" >29</td><td class="right " data-stat="yards_off" >368</td>
        <td class="right " data-stat="pass_yds_off" >265</td><td class="right " data-stat="rush_yds_off" >103</td>
        <td class="right iz" data-stat="to_off" ></td><td class="right " data-stat="first_down_def" >18</td>
        <td class="right " data-stat="yards_def" >378</td><td class="right " data-stat="pass_yds_def" >223</td>
        <td class="right " data-stat="rush_yds_def" >155</td><td class="right iz" data-stat="to_def" ></td>
        <td class="right " data-stat="exp_pts_off" >14.21</td><td class="right " data-stat="exp_pts_def" >-11.65</td>
        <td class="right " data-stat="exp_pts_st" >0.35</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2022-10-16" >October 16</td>
        <td class="right " data-stat="game_time" csk="16.25" >4:25PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202210160kan.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >L</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >4-2</td><td class="right iz" data-stat="game_location" ></td>
        <td class="left " data-stat="opp" ><a href="/teams/buf/2022.htm">Buffalo Bills</a></td>
        <td class="right " data-stat="pts_off" >20</td><td class="right " data-stat="pts_def" >24</td>
        <td class="right " data-stat="first_down_off" >23</td><td class="right " data-stat="yards_off" >387</td>
        <td class="right " data-stat="pass_yds_off" >319</td><td class="right " data-stat="rush_yds_off" >68</td>
        <td class="right " data-stat="to_off" >2</td><td class="right " data-stat="first_down_def" >26</td>
        <td class="right " data-stat="yards_def" >443</td><td class="right " data-stat="pass_yds_def" >318</td>
        <td class="right " data-stat="rush_yds_def" >125</td><td class="right " data-stat="to_def" >1</td>
        <td class="right " data-stat="exp_pts_off" >6.45</td><td class="right " data-stat="exp_pts_def" >-11.13</td>
        <td class="right " data-stat="exp_pts_st" >-0.56</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2022-10-23" >October 23</td>
        <td class="right " data-stat="game_time" csk="16.25" >4:25PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202210230sfo.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >5-2</td><td class="right " data-stat="game_location" >@</td>
        <td class="left " data-stat="opp" ><a href="/teams/sfo/2022.htm">San Francisco 49ers</a></td>
        <td class="right " data-stat="pts_off" >44</td><td class="right " data-stat="pts_def" >23</td>
        <td class="right " data-stat="first_down_off" >24</td><td class="right " data-stat="yards_off" >529</td>
        <td class="right " data-stat="pass_yds_off" >417</td><td class="right " data-stat="rush_yds_off" >112</td>
        <td class="right " data-stat="to_off" >2</td><td class="right " data-stat="first_down_def" >25</td>
        <td class="right " data-stat="yards_def" >444</td><td class="right " data-stat="pass_yds_def" >343</td>
        <td class="right " data-stat="rush_yds_def" >101</td><td class="right " data-stat="to_def" >3</td>
        <td class="right " data-stat="exp_pts_off" >30.58</td><td class="right " data-stat="exp_pts_def" >-3.59</td>
        <td class="right " data-stat="exp_pts_st" >-8.50</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="7.8" >8</th>
        <td class="left iz" data-stat="game_day_of_week" ></td><td class="left iz" data-stat="game_date" ></td>
        <td class="right iz" data-stat="game_time" ></td><td class="center iz" data-stat="boxscore_word" ></td>
        <td class="right iz" data-stat="game_outcome" ></td><td class="left iz" data-stat="overtime" ></td>
        <td class="center iz" data-stat="team_record" ></td><td class="right iz" data-stat="game_location" ></td>
        <td class="left " data-stat="opp" ><strong>Bye Week</strong></td><td class="right iz" data-stat="pts_off" ></td>
        <td class="right iz" data-stat="pts_def" ></td><td class="right iz" data-stat="first_down_off" ></td>
        <td class="right iz" data-stat="yards_off" ></td><td class="right iz" data-stat="pass_yds_off" ></td>
        <td class="right iz" data-stat="rush_yds_off" ></td><td class="right iz" data-stat="to_off" ></td>
        <td class="right iz" data-stat="first_down_def" ></td><td class="right iz" data-stat="yards_def" ></td>
        <td class="right iz" data-stat="pass_yds_def" ></td><td class="right iz" data-stat="rush_yds_def" ></td>
        <td class="right iz" data-stat="to_def" ></td><td class="right iz" data-stat="exp_pts_off" ></td>
        <td class="right iz" data-stat="exp_pts_def" ></td><td class="right iz" data-stat="exp_pts_st" ></td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2022-11-06" >November 6</td>
        <td class="right " data-stat="game_time" csk="20.20" >8:20PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202211060kan.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left " data-stat="overtime" >OT</td>
        <td class="center " data-stat="team_record" >6-2</td><td class="right iz" data-stat="game_location" ></td>
        <td class="left " data-stat="opp" ><a href="/teams/oti/2022.htm">Tennessee Titans</a></td>
        <td class="right " data-stat="pts_off" >20</td><td class="right " data-stat="pts_def" >17</td>
        <td class="right " data-stat="first_down_off" >29</td><td class="right " data-stat="yards_off" >499</td>
        <td class="right " data-stat="pass_yds_off" >422</td><td class="right " data-stat="rush_yds_off" >77</td>
        <td class="right " data-stat="to_off" >1</td><td class="right " data-stat="first_down_def" >9</td>
        <td class="right " data-stat="yards_def" >229</td><td class="right " data-stat="pass_yds_def" >57</td>
        <td class="right " data-stat="rush_yds_def" >172</td><td class="right iz" data-stat="to_def" ></td>
        <td class="right " data-stat="exp_pts_off" >5.59</td><td class="right " data-stat="exp_pts_def" >3.85</td>
        <td class="right " data-stat="exp_pts_st" >-5.59</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2022-11-13" >November 13</td>
        <td class="right " data-stat="game_time" csk="13.00" >1:00PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202211130kan.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >7-2</td><td class="right iz" data-stat="game_location" ></td>
        <td class="left " data-stat="opp" ><a href="/teams/jax/2022.htm">Jacksonville Jaguars</a></td>
        <td class="right " data-stat="pts_off" >27</td><td class="right " data-stat="pts_def" >17</td>
        <td class="right " data-stat="first_down_off" >26</td><td class="right " data-stat="yards_off" >486</td>
        <td class="right " data-stat="pass_yds_off" >331</td><td class="right " data-stat="rush_yds_off" >155</td>
        <td class="right " data-stat="to_off" >3</td><td class="right " data-stat="first_down_def" >17</td>
        <td class="right " data-stat="yards_def" >315</td><td class="right " data-stat="pass_yds_def" >240</td>
        <td class="right " data-stat="rush_yds_def" >75</td><td class="right iz" data-stat="to_def" ></td>
        <td class="right " data-stat="exp_pts_off" >23.27</td><td class="right " data-stat="exp_pts_def" >-3.86</td>
        <td class="right " data-stat="exp_pts_st" >-7.32</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2022-11-20" >November 20</td>
        <td class="right " data-stat="game_time" csk="20.20" >8:20PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202211200sdg.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >8-2</td><td class="right " data-stat="game_location" >@</td>
        <td class="left " data-stat="opp" ><a href="/teams/sdg/2022.htm">Los Angeles Chargers</a></td>
        <td class="right " data-stat="pts_off" >30</td><td class="right " data-stat="pts_def" >27</td>
        <td class="right " data-stat="first_down_off" >23</td><td class="right " data-stat="yards_off" >485</td>
        <td class="right " data-stat="pass_yds_off" >322</td><td class="right " data-stat="rush_yds_off" >163</td>
        <td class="right " data-stat="to_off" >1</td><td class="right " data-stat="first_down_def" >22</td>
        <td class="right " data-stat="yards_def" >365</td><td class="right " data-stat="pass_yds_def" >250</td>
        <td class="right " data-stat="rush_yds_def" >115</td><td class="right " data-stat="to_def" >2</td>
        <td class="right " data-stat="exp_pts_off" >19.64</td><td class="right " data-stat="exp_pts_def" >-8.61</td>
        <td class="right " data-stat="exp_pts_st" >-2.61</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2022-11-27" >November 27</td>
        <td class="right " data-stat="game_time" csk="16.25" >4:25PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202211270kan.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >9-2</td><td class="right iz" data-stat="game_location" ></td>
        <td class="left " data-stat="opp" ><a href="/teams/ram/2022.htm">Los Angeles Rams</a></td>
        <td class="right " data-stat="pts_off" >26</td><td class="right " data-stat="pts_def" >10</td>
        <td class="right " data-stat="first_down_off" >29</td><td class="right " data-stat="yards_off" >437</td>
        <td class="right " data-stat="pass_yds_off" >320</td><td class="right " data-stat="rush_yds_off" >117</td>
        <td class="right " data-stat="to_off" >2</td><td class="right " data-stat="first_down_def" >13</td>
        <td class="right " data-stat="yards_def" >198</td><td class="right " data-stat="pass_yds_def" >82</td>
        <td class="right " data-stat="rush_yds_def" >116</td><td class="right " data-stat="to_def" >2</td>
        <td class="right " data-stat="exp_pts_off" >13.96</td><td class="right " data-stat="exp_pts_def" >9.01</td>
        <td class="right " data-stat="exp_pts_st" >-8.76</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2022-12-04" >December 4</td>
        <td class="right " data-stat="game_time" csk="16.25" >4:25PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202212040cin.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >L</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >9-3</td><td class="right " data-stat="game_location" >@</td>
        <td class="left " data-stat="opp" ><a href="/teams/cin/2022.htm">Cincinnati Bengals</a></td>
        <td class="right " data-stat="pts_off" >24</td><td class="right " data-stat="pts_def" >27</td>
        <td class="right " data-stat="first_down_off" >20</td><td class="right " data-stat="yards_off" >349</td>
        <td class="right " data-stat="pass_yds_off" >211</td><td class="right " data-stat="rush_yds_off" >138</td>
        <td class="right " data-stat="to_off" >1</td><td class="right " data-stat="first_down_def" >26</td>
        <td class="right " data-stat="yards_def" >431</td><td class="right " data-stat="pass_yds_def" >279</td>
        <td class="right " data-stat="rush_yds_def" >152</td><td class="right iz" data-stat="to_def" ></td>
        <td class="right " data-stat="exp_pts_off" >16.21</td><td class="right " data-stat="exp_pts_def" >-19.79</td>
        <td class="right " data-stat="exp_pts_st" >-1.75</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2022-12-11" >December 11</td>
        <td class="right " data-stat="game_time" csk="16.20" >4:20PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202212110den.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >10-3</td><td class="right " data-stat="game_location" >@</td>
        <td class="left " data-stat="opp" ><a href="/teams/den/2022.htm">Denver Broncos</a></td>
        <td class="right " data-stat="pts_off" >34</td><td class="right " data-stat="pts_def" >28</td>
        <td class="right " data-stat="first_down_off" >20</td><td class="right " data-stat="yards_off" >431</td>
        <td class="right " data-stat="pass_yds_off" >342</td><td class="right " data-stat="rush_yds_off" >89</td>
        <td class="right " data-stat="to_off" >3</td><td class="right " data-stat="first_down_def" >17</td>
        <td class="right " data-stat="yards_def" >320</td><td class="right " data-stat="pass_yds_def" >214</td>
        <td class="right " data-stat="rush_yds_def" >106</td><td class="right " data-stat="to_def" >2</td>
        <td class="right " data-stat="exp_pts_off" >7.21</td><td class="right " data-stat="exp_pts_def" >0.63</td>
        <td class="right " data-stat="exp_pts_st" >-0.09</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2022-12-18" >December 18</td>
        <td class="right " data-stat="game_time" csk="13.00" >1:00PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202212180htx.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left " data-stat="overtime" >OT</td>
        <td class="center " data-stat="team_record" >11-3</td><td class="right " data-stat="game_location" >@</td>
        <td class="left " data-stat="opp" ><a href="/teams/htx/2022.htm">Houston Texans</a></td>
        <td class="right " data-stat="pts_off" >30</td><td class="right " data-stat="pts_def" >24</td>
        <td class="right " data-stat="first_down_off" >33</td><td class="right " data-stat="yards_off" >502</td>
        <td class="right " data-stat="pass_yds_off" >313</td><td class="right " data-stat="rush_yds_off" >189</td>
        <td class="right " data-stat="to_off" >2</td><td class="right " data-stat="first_down_def" >18</td>
        <td class="right " data-stat="yards_def" >219</td><td class="right " data-stat="pass_yds_def" >125</td>
        <td class="right " data-stat="rush_yds_def" >94</td><td class="right " data-stat="to_def" >1</td>
        <td class="right " data-stat="exp_pts_off" >13.62</td><td class="right " data-stat="exp_pts_def" >-2.21</td>
        <td class="right " data-stat="exp_pts_st" >-6.34</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th>
        <td class="left " data-stat="game_day_of_week" >Sat</td>
        <td class="left " data-stat="game_date" csk="2022-12-24" >December 24</td>
        <td class="right " data-stat="game_time" csk="13.00" >1:00PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202212240kan.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >12-3</td><td class="right iz" data-stat="game_location" ></td>
        <td class="left " data-stat="opp" ><a href="/teams/sea/2022.htm">Seattle Seahawks</a></td>
        <td class="right " data-stat="pts_off" >24</td><td class="right " data-stat="pts_def" >10</td>
        <td class="right " data-stat="first_down_off" >14</td><td class="right " data-stat="yards_off" >297</td>
        <td class="right " data-stat="pass_yds_off" >220</td><td class="right " data-stat="rush_yds_off" >77</td>
        <td class="right iz" data-stat="to_off" ></td><td class="right " data-stat="first_down_def" >19</td>
        <td class="right " data-stat="yards_def" >333</td><td class="right " data-stat="pass_yds_def" >200</td>
        <td class="right " data-stat="rush_yds_def" >133</td><td class="right " data-stat="to_def" >1</td>
        <td class="right " data-stat="exp_pts_off" >3.10</td><td class="right " data-stat="exp_pts_def" >11.64</td>
        <td class="right " data-stat="exp_pts_st" >-2.23</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2023-01-01" >January 1</td>
        <td class="right " data-stat="game_time" csk="13.00" >1:00PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202301010kan.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >13-3</td><td class="right iz" data-stat="game_location" ></td>
        <td class="left " data-stat="opp" ><a href="/teams/den/2022.htm">Denver Broncos</a></td>
        <td class="right " data-stat="pts_off" >27</td><td class="right " data-stat="pts_def" >24</td>
        <td class="right " data-stat="first_down_off" >22</td><td class="right " data-stat="yards_off" >374</td>
        <td class="right " data-stat="pass_yds_off" >328</td><td class="right " data-stat="rush_yds_off" >46</td>
        <td class="right " data-stat="to_off" >2</td><td class="right " data-stat="first_down_def" >21</td>
        <td class="right " data-stat="yards_def" >307</td><td class="right " data-stat="pass_yds_def" >190</td>
        <td class="right " data-stat="rush_yds_def" >117</td><td class="right " data-stat="to_def" >2</td>
        <td class="right " data-stat="exp_pts_off" >10.69</td><td class="right " data-stat="exp_pts_def" >2.92</td>
        <td class="right " data-stat="exp_pts_st" >-6.78</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th>
        <td class="left " data-stat="game_day_of_week" >Sat</td>
        <td class="left " data-stat="game_date" csk="2023-01-07" >January 7</td>
        <td class="right " data-stat="game_time" csk="16.30" >4:30PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202301070rai.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >14-3</td><td class="right " data-stat="game_location" >@</td>
        <td class="left " data-stat="opp" ><a href="/teams/rai/2022.htm">Las Vegas Raiders</a></td>
        <td class="right " data-stat="pts_off" >31</td><td class="right " data-stat="pts_def" >13</td>
        <td class="right " data-stat="first_down_off" >21</td><td class="right " data-stat="yards_off" >349</td>
        <td class="right " data-stat="pass_yds_off" >181</td><td class="right " data-stat="rush_yds_off" >168</td>
        <td class="right iz" data-stat="to_off" ></td><td class="right " data-stat="first_down_def" >21</td>
        <td class="right " data-stat="yards_def" >279</td><td class="right " data-stat="pass_yds_def" >180</td>
        <td class="right " data-stat="rush_yds_def" >99</td><td class="right " data-stat="to_def" >2</td>
        <td class="right " data-stat="exp_pts_off" >16.83</td><td class="right " data-stat="exp_pts_def" >5.67</td>
        <td class="right " data-stat="exp_pts_st" >-1.37</td></tr>
        <tr ><th scope="row" class="right iz" data-stat="week_num" csk="17.5" ></th>
        <td class="left iz" data-stat="game_day_of_week" ></td>
        <td class="left " data-stat="game_date" ><strong>Playoffs</strong></td>
        <td class="right iz" data-stat="game_time" ></td><td class="center iz" data-stat="boxscore_word" ></td>
        <td class="right iz" data-stat="game_outcome" ></td><td class="left iz" data-stat="overtime" ></td>
        <td class="center iz" data-stat="team_record" ></td><td class="right iz" data-stat="game_location" ></td>
        <td class="left iz" data-stat="opp" ></td><td class="right iz" data-stat="pts_off" ></td>
        <td class="right iz" data-stat="pts_def" ></td><td class="right iz" data-stat="first_down_off" ></td>
        <td class="right iz" data-stat="yards_off" ></td><td class="right iz" data-stat="pass_yds_off" ></td>
        <td class="right iz" data-stat="rush_yds_off" ></td><td class="right iz" data-stat="to_off" ></td>
        <td class="right iz" data-stat="first_down_def" ></td><td class="right iz" data-stat="yards_def" ></td>
        <td class="right iz" data-stat="pass_yds_def" ></td><td class="right iz" data-stat="rush_yds_def" ></td>
        <td class="right iz" data-stat="to_def" ></td><td class="right iz" data-stat="exp_pts_off" ></td>
        <td class="right iz" data-stat="exp_pts_def" ></td><td class="right iz" data-stat="exp_pts_st" ></td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="20" >Division</th>
        <td class="left " data-stat="game_day_of_week" >Sat</td>
        <td class="left " data-stat="game_date" csk="2023-01-21" >January 21</td>
        <td class="right " data-stat="game_time" csk="16.30" >4:30PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202301210kan.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >15-3</td><td class="right iz" data-stat="game_location" ></td>
        <td class="left " data-stat="opp" ><a href="/teams/jax/2022.htm">Jacksonville Jaguars</a></td>
        <td class="right " data-stat="pts_off" >27</td><td class="right " data-stat="pts_def" >20</td>
        <td class="right " data-stat="first_down_off" >23</td><td class="right " data-stat="yards_off" >362</td>
        <td class="right " data-stat="pass_yds_off" >218</td><td class="right " data-stat="rush_yds_off" >144</td>
        <td class="right iz" data-stat="to_off" ></td><td class="right " data-stat="first_down_def" >20</td>
        <td class="right " data-stat="yards_def" >349</td><td class="right " data-stat="pass_yds_def" >205</td>
        <td class="right " data-stat="rush_yds_def" >144</td><td class="right " data-stat="to_def" >2</td>
        <td class="right " data-stat="exp_pts_off" >13.73</td><td class="right " data-stat="exp_pts_def" >-4.86</td>
        <td class="right " data-stat="exp_pts_st" >-0.10</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="21" >Conf. Champ.</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2023-01-29" >January 29</td>
        <td class="right " data-stat="game_time" csk="18.30" >6:30PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202301290kan.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >16-3</td><td class="right iz" data-stat="game_location" ></td>
        <td class="left " data-stat="opp" ><a href="/teams/cin/2022.htm">Cincinnati Bengals</a></td>
        <td class="right " data-stat="pts_off" >23</td><td class="right " data-stat="pts_def" >20</td>
        <td class="right " data-stat="first_down_off" >23</td><td class="right " data-stat="yards_off" >357</td>
        <td class="right " data-stat="pass_yds_off" >315</td><td class="right " data-stat="rush_yds_off" >42</td>
        <td class="right " data-stat="to_off" >1</td><td class="right " data-stat="first_down_def" >18</td>
        <td class="right " data-stat="yards_def" >309</td><td class="right " data-stat="pass_yds_def" >238</td>
        <td class="right " data-stat="rush_yds_def" >71</td><td class="right " data-stat="to_def" >2</td>
        <td class="right " data-stat="exp_pts_off" >8.86</td><td class="right " data-stat="exp_pts_def" >-4.06</td>
        <td class="right " data-stat="exp_pts_st" >-3.07</td></tr>
        <tr ><th scope="row" class="right " data-stat="week_num" csk="22" >SuperBowl</th>
        <td class="left " data-stat="game_day_of_week" >Sun</td>
        <td class="left " data-stat="game_date" csk="2023-02-12" >February 12</td>
        <td class="right " data-stat="game_time" csk="18.30" >6:30PM ET</td>
        <td class="center " data-stat="boxscore_word" ><a href="/boxscores/202302120phi.htm">boxscore</a></td>
        <td class="right " data-stat="game_outcome" >W</td><td class="left iz" data-stat="overtime" ></td>
        <td class="center " data-stat="team_record" >17-3</td><td class="right " data-stat="game_location" >N</td>
        <td class="left " data-stat="opp" ><a href="/teams/phi/2022.htm">Philadelphia Eagles</a></td>
        <td class="right " data-stat="pts_off" >38</td><td class="right " data-stat="pts_def" >35</td>
        <td class="right " data-stat="first_down_off" >21</td><td class="right " data-stat="yards_off" >340</td>
        <td class="right " data-stat="pass_yds_off" >182</td><td class="right " data-stat="rush_yds_off" >158</td>
        <td class="right iz" data-stat="to_off" ></td><td class="right " data-stat="first_down_def" >25</td>
        <td class="right " data-stat="yards_def" >417</td><td class="right " data-stat="pass_yds_def" >302</td>
        <td class="right " data-stat="rush_yds_def" >115</td><td class="right " data-stat="to_def" >1</td>
        <td class="right " data-stat="exp_pts_off" >19.20</td><td class="right " data-stat="exp_pts_def" >-16.09</td>
        <td class="right " data-stat="exp_pts_st" >0.10</td></tr>
        </table>
        """

        soup = BeautifulSoup(fake_html, 'html.parser')
        df = t.collect_data(soup, 2022, 'Kansas City Chiefs')
        print(df)
        # the Chiefs played in 17 regular season games and averaged ~29.2 points in those games
        assert len(df.index) == 17 and int(df['points_for'].mean()) == 29

    def test_calculate_distance(self):
        city1 = {'latitude': 33.9416, 'longitude': 118.4085, 'airport': 'LAX'}
        city2 = {'latitude': 40.4919, 'longitude': 80.2352, 'airport': 'PIT'}
        assert int(t.calculate_distance(city1, city2)) == 2131
