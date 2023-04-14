# Player Splits

In order to retrieve a player's splits in a given season, you will first need to know the name of the player you are interested in. The spelling of the player's name must exactly match its spelling on [Pro Football Reference](https://www.pro-football-reference.com/). You will also need to specify the season you are interested in, as well as if you want the stats as averages or sums.

## Home-Road Splits

You can retrieve a player's stats in home vs. road games either as averages or sums.

### Averages

The following code will output Saquon Barkley's stats in home vs. road games in the 2018 season as averages.

```python

from pro_football_reference_web_scraper import player_splits as p

print(p.home_road(player = 'Saquon Barkley', position = 'RB', season = 2018, avg = True))

```

Output:

```

| game_location   |   games |   team_pts |   opp_pts |   rush_att |   rush_yds |   rush_td |   tgt |   rec_yds |   rec_td |
|:----------------|--------:|-----------:|----------:|-----------:|-----------:|----------:|------:|----------:|---------:|
| home            |       8 |     20.25  |     27.75 |     17     |     90.625 |     0.75  | 7.625 |    42.375 |    0.125 |
| away            |       8 |     25.875 |     23.75 |     15.625 |     72.75  |     0.625 | 7.5   |    47.75  |    0.375 |

```

### Sums

The following code will output Saquon Barkley's stats in home vs. road games in the 2018 season as sums.

```python

from pro_football_reference_web_scraper import player_splits as p

print(p.home_road(player = 'Saquon Barkley', position = 'RB', season = 2018, avg = False))

```

Output:

```

| game_location   |   games |   team_pts |   opp_pts |   rush_att |   rush_yds |   rush_td |   tgt |   rec_yds |   rec_td |
|:----------------|--------:|-----------:|----------:|-----------:|-----------:|----------:|------:|----------:|---------:|
| home            |       8 |        162 |       222 |        136 |        725 |         6 |    61 |       339 |        1 |
| away            |       8 |        207 |       190 |        125 |        582 |         5 |    60 |       382 |        3 |

```

## Win-Loss Splits

You can also retrieve a player's stats in wins vs. losses either as averages or sums.

### Averages

The following code will output Saquon Barkley's stats in wins vs. losses in the 2018 season as averages.


```python

from pro_football_reference_web_scraper import player_splits as p

print(p.win_loss(player = 'Saquon Barkley', position = 'RB', season = 2018, avg = True))

```

Output:

```

| result   |   games |   team_pts |   opp_pts |   rush_att |   rush_yds |   rush_td |   tgt |   rec_yds |   rec_td |
|:---------|--------:|-----------:|----------:|-----------:|-----------:|----------:|------:|----------:|---------:|
| W        |       5 |    32.4    |   24.6    |    20.4    |   117.2    |  0.8      |   4.4 |   25.2    | 0.2      |
| L        |      11 |    18.8182 |   26.2727 |    14.4545 |    65.5455 |  0.636364 |   9   |   54.0909 | 0.272727 |

```

### Sums

The following code will output Saquon Barkley's stats in wins vs. losses in the 2018 season as sums.

```python

from pro_football_reference_web_scraper import player_splits as p

print(p.win_loss(player = 'Saquon Barkley', position = 'RB', season = 2018, avg = False))

```

Output:

```

| result   |   games |   team_pts |   opp_pts |   rush_att |   rush_yds |   rush_td |   tgt |   rec_yds |   rec_td |
|:---------|--------:|-----------:|----------:|-----------:|-----------:|----------:|------:|----------:|---------:|
| W        |       5 |        162 |       123 |        102 |        586 |         4 |    22 |       126 |        1 |
| L        |      11 |        207 |       289 |        159 |        721 |         7 |    99 |       595 |        3 |

```