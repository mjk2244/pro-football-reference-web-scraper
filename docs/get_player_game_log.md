# Getting a Player's Game Log

In order to retrieve a player's game log in a given season, you will first need to know the name of the player you are interested in. The spelling of the player's name must exactly match its spelling on [Pro Football Reference](https://www.pro-football-reference.com/). You will also need to specify the season you are interested in as well as the player's position. We currently only support game logs for quarterbacks, running backs, wide receivers, and tight ends.

## QB Game Log

The following code will output Patrick Mahomes' game log from the 2022 season.

```eval_rst

.. note:: The `position` parameter must be 'QB' exactly. 'Quarterback' or 'qb' will not work.

```

```python

from pro_football_reference_web_scraper import player_game_log as p

print(p.get_player_game_log(player = 'Patrick Mahomes', position = 'QB', season = 2022))

```

Output:

```

|    | date       |   week | team   | game_location   | opp   | result   |   team_pts |   opp_pts |   cmp |   att |   pass_yds |   pass_td |   int |   rating |   sacked |   rush_att |   rush_yds |   rush_td |
|---:|:-----------|-------:|:-------|:----------------|:------|:---------|-----------:|----------:|------:|------:|-----------:|----------:|------:|---------:|---------:|-----------:|-----------:|----------:|
|  0 | 2022-09-11 |      1 | KAN    | @               | ARI   | W        |         44 |        21 |    30 |    39 |        360 |         5 |     0 |    144.2 |        0 |          3 |          5 |         0 |
|  1 | 2022-09-15 |      2 | KAN    |                 | LAC   | W        |         27 |        24 |    24 |    35 |        235 |         2 |     0 |    106.2 |        1 |          2 |         -1 |         0 |
|  2 | 2022-09-25 |      3 | KAN    | @               | IND   | L        |         17 |        20 |    20 |    35 |        262 |         1 |     1 |     78.5 |        1 |          4 |         26 |         0 |
|  3 | 2022-10-02 |      4 | KAN    | @               | TAM   | W        |         41 |        31 |    23 |    37 |        249 |         3 |     1 |     97.7 |        3 |          4 |         34 |         0 |
|  4 | 2022-10-10 |      5 | KAN    |                 | LVR   | W        |         30 |        29 |    29 |    43 |        292 |         4 |     0 |    117.6 |        3 |          4 |         28 |         0 |
|  5 | 2022-10-16 |      6 | KAN    |                 | BUF   | L        |         20 |        24 |    25 |    40 |        338 |         2 |     2 |     85.2 |        3 |          4 |         21 |         0 |
|  6 | 2022-10-23 |      7 | KAN    | @               | SFO   | W        |         44 |        23 |    25 |    34 |        423 |         3 |     1 |    132.4 |        1 |          0 |          0 |         0 |
|  7 | 2022-11-06 |      9 | KAN    |                 | TEN   | W        |         20 |        17 |    43 |    68 |        446 |         1 |     1 |     80.9 |        4 |          6 |         63 |         1 |
|  8 | 2022-11-13 |     10 | KAN    |                 | JAX   | W        |         27 |        17 |    26 |    35 |        331 |         4 |     1 |    129.6 |        0 |          7 |         39 |         0 |
|  9 | 2022-11-20 |     11 | KAN    | @               | LAC   | W        |         30 |        27 |    20 |    34 |        329 |         3 |     0 |    120.8 |        1 |          4 |         23 |         0 |
| 10 | 2022-11-27 |     12 | KAN    |                 | LAR   | W        |         26 |        10 |    27 |    42 |        320 |         1 |     1 |     85.4 |        0 |          4 |         36 |         0 |
| 11 | 2022-12-04 |     13 | KAN    | @               | CIN   | L        |         24 |        27 |    16 |    27 |        223 |         1 |     0 |     98.2 |        2 |          2 |          9 |         1 |
| 12 | 2022-12-11 |     14 | KAN    | @               | DEN   | W        |         34 |        28 |    28 |    42 |        352 |         3 |     3 |     86.6 |        2 |          3 |         -3 |         0 |
| 13 | 2022-12-18 |     15 | KAN    | @               | HOU   | W        |         30 |        24 |    36 |    41 |        336 |         2 |     0 |    117.1 |        2 |          5 |         33 |         1 |
| 14 | 2022-12-24 |     16 | KAN    |                 | SEA   | W        |         24 |        10 |    16 |    28 |        224 |         2 |     0 |    106.8 |        1 |          2 |          8 |         1 |
| 15 | 2023-01-01 |     17 | KAN    |                 | DEN   | W        |         27 |        24 |    29 |    42 |        328 |         3 |     1 |    106.1 |        0 |          4 |          8 |         0 |
| 16 | 2023-01-07 |     18 | KAN    | @               | LVR   | W        |         31 |        13 |    18 |    26 |        202 |         1 |     0 |    105   |        2 |          3 |         29 |         0 |

```

## RB Game Log

The following code will output Christian McCaffrey's game log from the 2019 season.

```eval_rst

.. note:: The `position` parameter must be 'RB' exactly. 'Running back' or 'rb' will not work.

```

```python

from pro_football_reference_web_scraper import player_game_log as p

print(p.get_player_game_log(player = 'Christian McCaffrey', position = 'RB', season = 2019))

```

Output:

```

|    | date       |   week | team   | game_location   | opp   | result   |   team_pts |   opp_pts |   rush_att |   rush_yds |   rush_td |   tgt |   rec |   rec_yds |   rec_td |
|---:|:-----------|-------:|:-------|:----------------|:------|:---------|-----------:|----------:|-----------:|-----------:|----------:|------:|------:|----------:|---------:|
|  0 | 2019-09-08 |      1 | CAR    |                 | LAR   | L        |         27 |        30 |         19 |        128 |         2 |    11 |    10 |        81 |        0 |
|  1 | 2019-09-12 |      2 | CAR    |                 | TAM   | L        |         14 |        20 |         16 |         37 |         0 |     6 |     2 |        16 |        0 |
|  2 | 2019-09-22 |      3 | CAR    | @               | ARI   | W        |         38 |        20 |         24 |        153 |         1 |     4 |     3 |        35 |        0 |
|  3 | 2019-09-29 |      4 | CAR    | @               | HOU   | W        |         16 |        10 |         27 |         93 |         1 |    10 |    10 |        86 |        0 |
|  4 | 2019-10-06 |      5 | CAR    |                 | JAX   | W        |         34 |        27 |         19 |        176 |         2 |     8 |     6 |        61 |        1 |
|  5 | 2019-10-13 |      6 | CAR    | @               | TAM   | W        |         37 |        26 |         22 |         31 |         1 |     5 |     4 |        26 |        1 |
|  6 | 2019-10-27 |      8 | CAR    | @               | SFO   | L        |         13 |        51 |         14 |        117 |         1 |     5 |     4 |        38 |        0 |
|  7 | 2019-11-03 |      9 | CAR    |                 | TEN   | W        |         30 |        20 |         24 |        146 |         2 |     3 |     3 |        20 |        1 |
|  8 | 2019-11-10 |     10 | CAR    | @               | GNB   | L        |         16 |        24 |         20 |        108 |         1 |     7 |     6 |        33 |        0 |
|  9 | 2019-11-17 |     11 | CAR    |                 | ATL   | L        |          3 |        29 |         14 |         70 |         0 |    15 |    11 |       121 |        0 |
| 10 | 2019-11-24 |     12 | CAR    | @               | NOR   | L        |         31 |        34 |         22 |         64 |         1 |     9 |     9 |        69 |        1 |
| 11 | 2019-12-01 |     13 | CAR    |                 | WAS   | L        |         21 |        29 |         14 |         44 |         0 |    12 |     7 |        58 |        0 |
| 12 | 2019-12-08 |     14 | CAR    | @               | ATL   | L        |         20 |        40 |         11 |         53 |         0 |    12 |    11 |        82 |        0 |
| 13 | 2019-12-15 |     15 | CAR    |                 | SEA   | L        |         24 |        30 |         19 |         87 |         2 |    10 |     8 |        88 |        0 |
| 14 | 2019-12-22 |     16 | CAR    | @               | IND   | L        |          6 |        38 |         13 |         54 |         0 |    15 |    15 |       119 |        0 |
| 15 | 2019-12-29 |     17 | CAR    |                 | NOR   | L        |         10 |        42 |          9 |         26 |         1 |    10 |     7 |        72 |        0 |

```

## WR Game Log

The following code will output Jordy Nelson's game log from the 2014 season.

```eval_rst

.. note:: The `position` parameter must be 'WR' exactly. 'Wide receiver' or 'wr' will not work.

```

```python

from pro_football_reference_web_scraper import player_game_log as p

print(p.get_player_game_log(player = 'Jordy Nelson', position = 'WR', season = 2014))

```

Output:

```

|    | date       |   week | team   | game_location   | opp   | result   |   team_pts |   opp_pts |   tgt |   rec |   rec_yds |   rec_td |   snap_pct |
|---:|:-----------|-------:|:-------|:----------------|:------|:---------|-----------:|----------:|------:|------:|----------:|---------:|-----------:|
|  0 | 2014-09-04 |      1 | GNB    | @               | SEA   | L        |         16 |        36 |    14 |     9 |        83 |        0 |       0.98 |
|  1 | 2014-09-14 |      2 | GNB    |                 | NYJ   | W        |         31 |        24 |    16 |     9 |       209 |        1 |       0.97 |
|  2 | 2014-09-21 |      3 | GNB    | @               | DET   | L        |          7 |        19 |     7 |     5 |        59 |        0 |       1    |
|  3 | 2014-09-28 |      4 | GNB    | @               | CHI   | W        |         38 |        17 |    12 |    10 |       108 |        2 |       1    |
|  4 | 2014-10-02 |      5 | GNB    |                 | MIN   | W        |         42 |        10 |     3 |     1 |        66 |        1 |       0.7  |
|  5 | 2014-10-12 |      6 | GNB    | @               | MIA   | W        |         27 |        24 |    16 |     9 |       107 |        1 |       1    |
|  6 | 2014-10-19 |      7 | GNB    |                 | CAR   | W        |         38 |        17 |     5 |     4 |        80 |        1 |       0.84 |
|  7 | 2014-10-26 |      8 | GNB    | @               | NOR   | L        |         23 |        44 |     5 |     3 |        25 |        0 |       0.93 |
|  8 | 2014-11-09 |     10 | GNB    |                 | CHI   | W        |         55 |        14 |     6 |     6 |       152 |        2 |       0.63 |
|  9 | 2014-11-16 |     11 | GNB    |                 | PHI   | W        |         53 |        20 |    10 |     4 |       109 |        1 |       0.76 |
| 10 | 2014-11-23 |     12 | GNB    | @               | MIN   | W        |         24 |        21 |    12 |     8 |        68 |        0 |       0.95 |
| 11 | 2014-11-30 |     13 | GNB    |                 | NWE   | W        |         26 |        21 |     6 |     2 |        53 |        1 |       1    |
| 12 | 2014-12-08 |     14 | GNB    |                 | ATL   | W        |         43 |        37 |    10 |     8 |       146 |        2 |       0.99 |
| 13 | 2014-12-14 |     15 | GNB    | @               | BUF   | L        |         13 |        21 |    12 |     5 |        55 |        0 |       0.99 |
| 14 | 2014-12-21 |     16 | GNB    | @               | TAM   | W        |         20 |         3 |     9 |     9 |       113 |        1 |       0.89 |
| 15 | 2014-12-28 |     17 | GNB    |                 | DET   | W        |         30 |        20 |     8 |     6 |        86 |        0 |       0.94 |

```

## TE Game Log

The following code will output Jimmy Graham's game log from the 2013 season.

```eval_rst

.. note:: The `position` parameter must be 'TE' exactly. 'Tight end' or 'te' will not work.

```

```python

from pro_football_reference_web_scraper import player_game_log as p

print(p.get_player_game_log(player = 'Jimmy Graham', position = 'TE', season = 2013))

```

Output:

```

|    | date       |   week | team   | game_location   | opp   | result   |   team_pts |   opp_pts |   tgt |   rec |   rec_yds |   rec_td |   snap_pct |
|---:|:-----------|-------:|:-------|:----------------|:------|:---------|-----------:|----------:|------:|------:|----------:|---------:|-----------:|
|  0 | 2013-09-08 |      1 | NOR    |                 | ATL   | W        |         23 |        17 |     7 |     4 |        45 |        1 |       0.83 |
|  1 | 2013-09-15 |      2 | NOR    | @               | TAM   | W        |         16 |        14 |    16 |    10 |       179 |        1 |       0.81 |
|  2 | 2013-09-22 |      3 | NOR    |                 | ARI   | W        |         31 |         7 |    15 |     9 |       134 |        2 |       0.8  |
|  3 | 2013-09-30 |      4 | NOR    |                 | MIA   | W        |         38 |        17 |     4 |     4 |       100 |        2 |       0.78 |
|  4 | 2013-10-06 |      5 | NOR    | @               | CHI   | W        |         26 |        18 |    11 |    10 |       135 |        0 |       0.55 |
|  5 | 2013-10-13 |      6 | NOR    | @               | NWE   | L        |         27 |        30 |     6 |     0 |         0 |        0 |       0.69 |
|  6 | 2013-10-27 |      8 | NOR    |                 | BUF   | W        |         35 |        17 |     3 |     3 |        37 |        2 |       0.26 |
|  7 | 2013-11-03 |      9 | NOR    | @               | NYJ   | L        |         20 |        26 |    12 |     9 |       116 |        2 |       0.76 |
|  8 | 2013-11-10 |     10 | NOR    |                 | DAL   | W        |         49 |        17 |     5 |     5 |        59 |        0 |       0.39 |
|  9 | 2013-11-17 |     11 | NOR    |                 | SFO   | W        |         23 |        20 |    11 |     6 |        41 |        0 |       0.74 |
| 10 | 2013-11-21 |     12 | NOR    | @               | ATL   | W        |         17 |        13 |     7 |     5 |       100 |        1 |       0.63 |
| 11 | 2013-12-02 |     13 | NOR    | @               | SEA   | L        |          7 |        34 |     9 |     3 |        42 |        1 |       0.88 |
| 12 | 2013-12-08 |     14 | NOR    |                 | CAR   | W        |         31 |        13 |    11 |     6 |        58 |        2 |       0.72 |
| 13 | 2013-12-15 |     15 | NOR    | @               | STL   | L        |         16 |        27 |     6 |     2 |        25 |        0 |       0.84 |
| 14 | 2013-12-22 |     16 | NOR    | @               | CAR   | L        |         13 |        17 |    11 |     5 |        73 |        1 |       0.54 |
| 15 | 2013-12-29 |     17 | NOR    |                 | TAM   | W        |         42 |        17 |     8 |     5 |        71 |        1 |       0.52 |

```
