# Team Splits

In order to retrieve a team's splits in a given season, you will first need to know the name of the team you are interested in. The spelling of the team's name must exactly match its spelling on [Pro Football Reference](https://www.pro-football-reference.com/). You will also need to specify the season you are interested in, as well as if you want the stats as averages or sums.

## Home-Road Splits

You can retrieve a team's stats in home vs. road games either as averages or sums.

### Averages

The following code will output the Philadelphia Eagles stats in home vs. road games in the 2018 season as averages.

```eval_rst

.. note:: The 'team' parameter is case sensitive. 'Philadelphia eagles' will not work, but 'Philadelphia Ealges' will.

```

```python

from pro_football_reference_web_scraper import team_splits as t

print(t.home_road(team = 'Philadelphia Eagles', season = 2018, avg = True))

```

Output:

```

| game_location   |   games |   wins |   ties |   losses |   points_for |   points_allowed |   tot_yds |   pass_yds |   rush_yds |   opp_tot_yds |   opp_pass_yds |   opp_rush_yds |
|:----------------|--------:|-------:|-------:|---------:|-------------:|-----------------:|----------:|-----------:|-----------:|--------------:|---------------:|---------------:|
| home            |       8 |      5 |      0 |        3 |       22.625 |             20.5 |   379.25  |    280.625 |     98.625 |       334     |        233.625 |        100.375 |
| away            |       8 |      4 |      0 |        4 |       23.25  |             23   |   351.375 |    253.75  |     97.625 |       398.375 |        304.875 |         93.5   |

```

### Sums

The following code will output the Philadelphia Eagles stats in home vs. road games in the 2018 season as sums.

```eval_rst

.. note:: The 'team' parameter is case sensitive. 'Philadelphia eagles' will not work, but 'Philadelphia Ealges' will.

```

```python

from pro_football_reference_web_scraper import team_splits as t

print(t.home_road(team = 'Philadelphia Eagles', season = 2018, avg = False))

```

Output:

```

| game_location   |   games |   wins |   ties |   losses |   points_for |   points_allowed |   tot_yds |   pass_yds |   rush_yds |   opp_tot_yds |   opp_pass_yds |   opp_rush_yds |
|:----------------|--------:|-------:|-------:|---------:|-------------:|-----------------:|----------:|-----------:|-----------:|--------------:|---------------:|---------------:|
| home            |       8 |      5 |      0 |        3 |          181 |              164 |      3034 |       2245 |        789 |          2672 |           1869 |            803 |
| away            |       8 |      4 |      0 |        4 |          186 |              184 |      2811 |       2030 |        781 |          3187 |           2439 |            748 |

```

## Win-Loss Splits

You can also retrieve a team's stats in wins vs. losses either as averages or sums.

### Averages

The following code will output the Philadelphia Eagles stats in wins vs. losses games in the 2018 season as averages.

```eval_rst

.. note:: The 'team' parameter is case sensitive. 'Philadelphia eagles' will not work, but 'Philadelphia Ealges' will.

```

```python

from pro_football_reference_web_scraper import team_splits as t

print(t.win_loss(team = 'Philadelphia Eagles', season = 2018, avg = True))

```

Output:

```

| result   |   games |   points_for |   points_allowed |   tot_yds |   pass_yds |   rush_yds |   opp_tot_yds |   opp_pass_yds |   opp_rush_yds |
|:---------|--------:|-------------:|-----------------:|----------:|-----------:|-----------:|--------------:|---------------:|---------------:|
| W        |       9 |      26.1111 |          16.3333 |   380.222 |    262.444 |   117.778  |       305.333 |        221.556 |        83.7778 |
| L        |       7 |      18.8571 |          28.7143 |   346.143 |    273.286 |    72.8571 |       444.429 |        330.571 |       113.857  |

```

### Sums

The following code will output the Philadelphia Eagles stats in wins vs. lossees in the 2018 season as sums.

```eval_rst

.. note:: The 'team' parameter is case sensitive. 'Philadelphia eagles' will not work, but 'Philadelphia Ealges' will.

```

```python

from pro_football_reference_web_scraper import team_splits as t

print(t.win_loss(team = 'Philadelphia Eagles', season = 2018, avg = False))

```

Output:

```

| result   |   games |   points_for |   points_allowed |   tot_yds |   pass_yds |   rush_yds |   opp_tot_yds |   opp_pass_yds |   opp_rush_yds |
|:---------|--------:|-------------:|-----------------:|----------:|-----------:|-----------:|--------------:|---------------:|---------------:|
| W        |       9 |          235 |              147 |      3422 |       2362 |       1060 |          2748 |           1994 |            754 |
| L        |       7 |          132 |              201 |      2423 |       1913 |        510 |          3111 |           2314 |            797 |

```