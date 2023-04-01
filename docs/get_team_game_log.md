# Getting a Team's Game Log

In order to retrieve a team's game log in a given season, you will first need to know the name of the team you are interested in. The spelling of the team's name must exactly match its spelling on [Pro Football Reference](https://www.pro-football-reference.com/). You will also need to specify the season you are interested in. The following code will print the Los Angeles Rams' game log during the 2021 season. The bye week is omitted. In addition to more traditional stats, the game log also includes stats on distance traveled (if an away game) and number of rest days.

```eval_rst
.. note:: Please capitalize every word in the team's name. For example, 'los angeles rams' will not work, but 'Los Angeles Rams' will. Additionally, ensure that you are writing the team's entire name (e.g. 'Los Angeles Rams' instead of 'Rams').

```

```python

from pro_football_reference import team_game_log as t

print(t.get_team_game_log(team = 'Los Angeles Rams', season = 2021))

```

Output:

```
|    |   week | day   | rest_days        | home_team   |   distance_travelled | opp                  | result   |   points_for |   points_allowed |   tot_yds |   pass_yds |   rush_yds |   opp_tot_yds |   opp_pass_yds |   opp_rush_yds |
|---:|-------:|:------|:-----------------|:------------|---------------------:|:---------------------|:---------|-------------:|-----------------:|----------:|-----------:|-----------:|--------------:|---------------:|---------------:|
|  0 |      1 | Sun   | 10 days 00:00:00 | True        |                0     | Chicago Bears        | W        |           34 |               14 |       386 |        312 |         74 |           322 |            188 |            134 |
|  1 |      2 | Sun   | 7 days 00:00:00  | False       |             1809.97  | Indianapolis Colts   | W        |           27 |               24 |       371 |        270 |        101 |           354 |            245 |            109 |
|  2 |      3 | Sun   | 7 days 00:00:00  | True        |                0     | Tampa Bay Buccaneers | W        |           34 |               24 |       407 |        331 |         76 |           446 |            411 |             35 |
|  3 |      4 | Sun   | 7 days 00:00:00  | True        |                0     | Arizona Cardinals    | L        |           20 |               37 |       401 |        280 |        121 |           465 |            249 |            216 |
|  4 |      5 | Thu   | 4 days 00:00:00  | False       |              954.979 | Seattle Seahawks     | W        |           26 |               17 |       476 |        358 |        118 |           354 |            262 |             92 |
|  5 |      6 | Sun   | 10 days 00:00:00 | False       |             2448.6   | New York Giants      | W        |           38 |               11 |       365 |        234 |        131 |           261 |            201 |             60 |
|  6 |      7 | Sun   | 7 days 00:00:00  | True        |                0     | Detroit Lions        | W        |           28 |               19 |       374 |        327 |         47 |           415 |            278 |            137 |
|  7 |      8 | Sun   | 7 days 00:00:00  | False       |             1376.55  | Houston Texans       | W        |           38 |               22 |       467 |        302 |        165 |           323 |            279 |             44 |
|  8 |      9 | Sun   | 7 days 00:00:00  | True        |                0     | Tennessee Titans     | L        |           16 |               28 |       347 |        253 |         94 |           194 |            125 |             69 |
|  9 |     10 | Mon   | 8 days 00:00:00  | False       |              308.127 | San Francisco 49ers  | L        |           10 |               31 |       278 |        226 |         52 |           335 |            179 |            156 |
| 10 |     12 | Sun   | 13 days 00:00:00 | False       |             1764.03  | Green Bay Packers    | L        |           28 |               36 |       353 |        285 |         68 |           399 |            307 |             92 |
| 11 |     13 | Sun   | 7 days 00:00:00  | True        |                0     | Jacksonville Jaguars | W        |           37 |                7 |       418 |        290 |        128 |           197 |            136 |             61 |
| 12 |     14 | Mon   | 8 days 00:00:00  | False       |              369.445 | Arizona Cardinals    | W        |           30 |               23 |       356 |        267 |         89 |           447 |            344 |            103 |
| 13 |     15 | Tue   | 8 days 00:00:00  | True        |                0     | Seattle Seahawks     | W        |           20 |               10 |       332 |        209 |        123 |           214 |            134 |             80 |
| 14 |     16 | Sun   | 5 days 00:00:00  | False       |             1533.21  | Minnesota Vikings    | W        |           30 |               23 |       356 |        197 |        159 |           361 |            295 |             66 |
| 15 |     17 | Sun   | 7 days 00:00:00  | False       |             2323.91  | Baltimore Ravens     | W        |           20 |               19 |       373 |        300 |         73 |           327 |            162 |            165 |
| 16 |     18 | Sun   | 7 days 00:00:00  | True        |                0     | San Francisco 49ers  | L        |           24 |               27 |       265 |        201 |         64 |           449 |            314 |            135 |
```

## Teams That Changed Names

Some teams have changed names throughout the course of NFL history. For example, the Phoenix Cardinals became the Arizona Cardinals in 1984. If you are unsure of when a team changed its name, you can either use any of its historical names or its current name. For example, the following code blocks will give the same output.

```python

from pro_football_reference_web_scraper import team_game_log as t

print(t.get_team_game_log(team = 'Phoenix Cardinals', season = 1994))

```

```python

from pro_football_reference_web_scraper import team_game_log as t

print(t.get_team_game_log(team = 'Arizona Cardinals', season = 1994))

```

Output:

```

|    |   week | day   | rest_days        | home_team   |   distance_travelled | opp                 | result   |   points_for |   points_allowed |   tot_yds |   pass_yds |   rush_yds |   opp_tot_yds |   opp_pass_yds |   opp_rush_yds |
|---:|-------:|:------|:-----------------|:------------|---------------------:|:--------------------|:---------|-------------:|-----------------:|----------:|-----------:|-----------:|--------------:|---------------:|---------------:|
|  0 |      1 | Sun   | 10 days 00:00:00 | False       |              369.445 | Los Angeles Rams    | L        |           12 |               14 |       234 |        128 |        106 |           152 |            102 |             50 |
|  1 |      2 | Sun   | 7 days 00:00:00  | True        |                0     | New York Giants     | L        |           17 |               20 |       174 |        135 |         39 |           206 |             88 |            118 |
|  2 |      3 | Sun   | 7 days 00:00:00  | False       |             1733.7   | Cleveland Browns    | L        |            0 |               32 |       318 |        255 |         63 |           322 |            243 |             79 |
|  3 |      5 | Sun   | 14 days 00:00:00 | True        |                0     | Minnesota Vikings   | W        |           17 |                7 |       309 |        200 |        109 |           358 |            340 |             18 |
|  4 |      6 | Sun   | 7 days 00:00:00  | False       |              865.842 | Dallas Cowboys      | L        |            3 |               38 |       221 |        168 |         53 |           351 |            273 |             78 |
|  5 |      7 | Sun   | 7 days 00:00:00  | False       |             1951.93  | Washington Redskins | W        |           19 |               16 |       324 |        173 |        151 |           234 |            149 |             85 |
|  6 |      8 | Sun   | 7 days 00:00:00  | True        |                0     | Dallas Cowboys      | L        |           21 |               28 |       315 |        208 |        107 |           312 |            237 |             75 |
|  7 |      9 | Sun   | 7 days 00:00:00  | True        |                0     | Pittsburgh Steelers | W        |           20 |               17 |       335 |        236 |         99 |           317 |            232 |             85 |
|  8 |     10 | Sun   | 7 days 00:00:00  | False       |             2074.89  | Philadelphia Eagles | L        |            7 |               17 |       254 |        181 |         73 |           322 |            172 |            150 |
|  9 |     11 | Sun   | 7 days 00:00:00  | False       |             2127.99  | New York Giants     | W        |           10 |                9 |       239 |        173 |         66 |           231 |             81 |            150 |
| 10 |     12 | Sun   | 7 days 00:00:00  | True        |                0     | Philadelphia Eagles | W        |           12 |                6 |       281 |        123 |        158 |           185 |            110 |             75 |
| 11 |     13 | Sun   | 7 days 00:00:00  | True        |                0     | Chicago Bears       | L        |           16 |               19 |       244 |        177 |         67 |           318 |            186 |            132 |
| 12 |     14 | Sun   | 7 days 00:00:00  | False       |             1007.26  | Houston Oilers      | W        |           30 |               12 |       332 |        171 |        161 |           198 |            161 |             37 |
| 13 |     15 | Sun   | 7 days 00:00:00  | True        |                0     | Washington Redskins | W        |           17 |               15 |       278 |        194 |         84 |           406 |            283 |            123 |
| 14 |     16 | Sun   | 7 days 00:00:00  | True        |                0     | Cincinnati Bengals  | W        |           28 |                7 |       364 |        212 |        152 |           189 |            125 |             64 |
| 15 |     17 | Sat   | 6 days 00:00:00  | False       |             1583.8   | Atlanta Falcons     | L        |            6 |               10 |       385 |        313 |         72 |           307 |            256 |             51 |

```
