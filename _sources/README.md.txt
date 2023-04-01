# Quick Guide
Web scraper to retrieve player and team data from Pro Football Reference.  

[![](https://img.shields.io/github/license/mjk2244/pro-football-reference-web-scraper)](https://opensource.org/licenses/Apache-2.0) ![](https://img.shields.io/github/issues/mjk2244/pro-football-reference-web-scraper) [![](https://codecov.io/gh/mjk2244/pro-football-reference-web-scraper/branch/main/graph/badge.svg?token=OTGOR2M0CY)](https://codecov.io/gh/mjk2244/pro-football-reference-web-scraper) [![](https://img.shields.io/github/actions/workflow/status/mjk2244/pro-football-reference-web-scraper/build.yml)](https://github.com/mjk2244/pro-football-reference-web-scraper/) [![](https://img.shields.io/pypi/v/pro-football-reference-web-scraper)](https://pypi.org/project/pro-football-reference-web-scraper/)
## Overview
pro-football-reference-web-scraper is a Python library that helps developers take advantage of the plethora of free data provided by [Pro Football Reference](https://www.pro-football-reference.com/). It is intended primarily to help fantasy sports players and sports bettors gain an edge in their NFL sports gaming endeavors. However, it can be used for any project that requires team- and player-specific data.

## Installation
To install, run the following:
```
pip install pro-football-reference-web-scraper
```

## Usage
### Player Game Logs
The following code will retrieve and print Josh Allen's game log during the 2022 season as a pandas DataFrame.  

`player`: a player's full name, as it appears on [Pro Football Reference](https://www.pro-football-reference.com/)  
`position`: 'QB', 'RB', 'TE', or 'WR'  
`season`: the season you are looking for (int)  

```python
from pro_football_reference_web_scraper import player_game_log as p

game_log = p.get_player_game_log(player = 'Josh Allen', position = 'QB', season = 2022)
print(game_log)
```

### Team Game Logs
The following code will retrieve and print the Kansas City Chiefs' game log during the 1995 season as a pandas DataFrame.  

`team`: a team's full name (city and mascot), as it appears on [Pro Football Reference](https://www.pro-football-reference.com/)  
`season`: the season you are looking for (int)  

```python
from pro_football_reference_web_scraper import team_game_log as t

game_log = t.get_team_game_log(team = 'Kansas City Chiefs', season = 1995)
print(game_log)
```
