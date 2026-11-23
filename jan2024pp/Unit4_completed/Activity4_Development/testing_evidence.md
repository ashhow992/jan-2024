Actual automated execution of the Python program. Each test below includes observed output.

Test 1: Normal: five games, varied scores and times
Result: PASS
Actual console output:
Games club score recorder
Player ID: Number of games (5-10): Game 1
Score (0 or more): Time (5-60 whole minutes): Game 2
Score (0 or more): Time (5-60 whole minutes): Game 3
Score (0 or more): Time (5-60 whole minutes): Game 4
Score (0 or more): Time (5-60 whole minutes): Game 5
Score (0 or more): Time (5-60 whole minutes): Player ID: P01
Highest score: 50
Average time: 30 minutes
Record saved to player_scores.txt

Saved file:
Player ID: P01
Highest score: 50
Average time: 30 minutes
Number of games: 5
Game 1: score 10, time 10 minutes
Game 2: score 20, time 20 minutes
Game 3: score 30, time 30 minutes
Game 4: score 40, time 40 minutes
Game 5: score 50, time 50 minutes
---


Test 2: Extreme: ten games, maximum time
Result: PASS
Actual console output:
Games club score recorder
Player ID: Number of games (5-10): Game 1
Score (0 or more): Time (5-60 whole minutes): Game 2
Score (0 or more): Time (5-60 whole minutes): Game 3
Score (0 or more): Time (5-60 whole minutes): Game 4
Score (0 or more): Time (5-60 whole minutes): Game 5
Score (0 or more): Time (5-60 whole minutes): Game 6
Score (0 or more): Time (5-60 whole minutes): Game 7
Score (0 or more): Time (5-60 whole minutes): Game 8
Score (0 or more): Time (5-60 whole minutes): Game 9
Score (0 or more): Time (5-60 whole minutes): Game 10
Score (0 or more): Time (5-60 whole minutes): Player ID: P02
Highest score: 999999
Average time: 60 minutes
Record saved to player_scores.txt

Saved file:
Player ID: P02
Highest score: 999999
Average time: 60 minutes
Number of games: 10
Game 1: score 999999, time 60 minutes
Game 2: score 999999, time 60 minutes
Game 3: score 999999, time 60 minutes
Game 4: score 999999, time 60 minutes
Game 5: score 999999, time 60 minutes
Game 6: score 999999, time 60 minutes
Game 7: score 999999, time 60 minutes
Game 8: score 999999, time 60 minutes
Game 9: score 999999, time 60 minutes
Game 10: score 999999, time 60 minutes
---


Test 3: Extreme: minimum time and zero score
Result: PASS
Actual console output:
Games club score recorder
Player ID: Number of games (5-10): Game 1
Score (0 or more): Time (5-60 whole minutes): Game 2
Score (0 or more): Time (5-60 whole minutes): Game 3
Score (0 or more): Time (5-60 whole minutes): Game 4
Score (0 or more): Time (5-60 whole minutes): Game 5
Score (0 or more): Time (5-60 whole minutes): Player ID: P03
Highest score: 0
Average time: 5 minutes
Record saved to player_scores.txt

Saved file:
Player ID: P03
Highest score: 0
Average time: 5 minutes
Number of games: 5
Game 1: score 0, time 5 minutes
Game 2: score 0, time 5 minutes
Game 3: score 0, time 5 minutes
Game 4: score 0, time 5 minutes
Game 5: score 0, time 5 minutes
---


Test 4: Abnormal: blank ID, invalid game counts
Result: PASS
Actual console output:
Games club score recorder
Player ID: Player ID cannot be blank.
Player ID: Number of games (5-10): Invalid whole number or range. Try again.
Number of games (5-10): Invalid whole number or range. Try again.
Number of games (5-10): Invalid whole number or range. Try again.
Number of games (5-10): Game 1
Score (0 or more): Time (5-60 whole minutes): Game 2
Score (0 or more): Time (5-60 whole minutes): Game 3
Score (0 or more): Time (5-60 whole minutes): Game 4
Score (0 or more): Time (5-60 whole minutes): Game 5
Score (0 or more): Time (5-60 whole minutes): Player ID: P04
Highest score: 50
Average time: 30 minutes
Record saved to player_scores.txt

Saved file:
Player ID: P04
Highest score: 50
Average time: 30 minutes
Number of games: 5
Game 1: score 10, time 10 minutes
Game 2: score 20, time 20 minutes
Game 3: score 30, time 30 minutes
Game 4: score 40, time 40 minutes
Game 5: score 50, time 50 minutes
---


Test 5: Abnormal: invalid scores and times
Result: PASS
Actual console output:
Games club score recorder
Player ID: Number of games (5-10): Game 1
Score (0 or more): Invalid whole number or range. Try again.
Score (0 or more): Invalid whole number or range. Try again.
Score (0 or more): Invalid whole number or range. Try again.
Score (0 or more): Time (5-60 whole minutes): Invalid whole number or range. Try again.
Time (5-60 whole minutes): Invalid whole number or range. Try again.
Time (5-60 whole minutes): Invalid whole number or range. Try again.
Time (5-60 whole minutes): Invalid whole number or range. Try again.
Time (5-60 whole minutes): Game 2
Score (0 or more): Time (5-60 whole minutes): Game 3
Score (0 or more): Time (5-60 whole minutes): Game 4
Score (0 or more): Time (5-60 whole minutes): Game 5
Score (0 or more): Time (5-60 whole minutes): Player ID: P05
Highest score: 50
Average time: 30 minutes
Record saved to player_scores.txt

Saved file:
Player ID: P05
Highest score: 50
Average time: 30 minutes
Number of games: 5
Game 1: score 10, time 10 minutes
Game 2: score 20, time 20 minutes
Game 3: score 30, time 30 minutes
Game 4: score 40, time 40 minutes
Game 5: score 50, time 50 minutes
---


Test 6: Rounding: fractional average
Result: PASS
Actual console output:
Games club score recorder
Player ID: Number of games (5-10): Game 1
Score (0 or more): Time (5-60 whole minutes): Game 2
Score (0 or more): Time (5-60 whole minutes): Game 3
Score (0 or more): Time (5-60 whole minutes): Game 4
Score (0 or more): Time (5-60 whole minutes): Game 5
Score (0 or more): Time (5-60 whole minutes): Player ID: P06
Highest score: 2
Average time: 6 minutes
Record saved to player_scores.txt

Saved file:
Player ID: P06
Highest score: 2
Average time: 6 minutes
Number of games: 5
Game 1: score 1, time 5 minutes
Game 2: score 1, time 5 minutes
Game 3: score 2, time 6 minutes
Game 4: score 2, time 6 minutes
Game 5: score 2, time 6 minutes
---


Test 7: Append | PASS
Player ID: P01
Highest score: 50
Average time: 30 minutes
Number of games: 5
Game 1: score 10, time 10 minutes
Game 2: score 20, time 20 minutes
Game 3: score 30, time 30 minutes
Game 4: score 40, time 40 minutes
Game 5: score 50, time 50 minutes
---
Player ID: P03
Highest score: 0
Average time: 5 minutes
Number of games: 5
Game 1: score 0, time 5 minutes
Game 2: score 0, time 5 minutes
Game 3: score 0, time 5 minutes
Game 4: score 0, time 5 minutes
Game 5: score 0, time 5 minutes
---


Test 8: File error | PASS
Games club score recorder
Player ID: Number of games (5-10): Game 1
Score (0 or more): Time (5-60 whole minutes): Game 2
Score (0 or more): Time (5-60 whole minutes): Game 3
Score (0 or more): Time (5-60 whole minutes): Game 4
Score (0 or more): Time (5-60 whole minutes): Game 5
Score (0 or more): Time (5-60 whole minutes): Player ID: P01
Highest score: 50
Average time: 30 minutes
Could not save record to player_scores.txt


Summary: 8/8 tests passed. No failed tests requiring a code fix were observed in this run. Console transcripts are evidence, not screenshots.