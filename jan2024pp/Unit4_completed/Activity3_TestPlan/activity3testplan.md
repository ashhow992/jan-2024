Design assumptions: non-blank ID; non-negative whole-number scores with no specified maximum; average rounded to nearest whole minute (half up). Each test uses a fresh file. Input pairs are score, minutes.

Test 1: Normal: five games, varied scores and times
Data: 'P01', '5', '10', '10', '20', '20', '30', '30', '40', '40', '50', '50'
Expected: Highest score: 50; Average time: 30 minutes; correct ID and all records saved. 

Test 2: Extreme: ten games, maximum time
Data: 'P02', '10', '999999', '60', '999999', '60', '999999', '60', '999999', '60', '999999', '60', '999999', '60', '999999', '60', '999999', '60', '999999', '60', '999999', '60'
Expected: Highest score: 999999; Average time: 60 minutes; correct ID and all records saved. 

Test 3: Extreme: minimum time and zero score
Data: 'P03', '5', '0', '5', '0', '5', '0', '5', '0', '5', '0', '5'
Expected: Highest score: 0; Average time: 5 minutes; correct ID and all records saved. 

Test 4: Abnormal: blank ID, invalid game counts
Data: '', 'P04', '4', '11', 'abc', '5', '10', '10', '20', '20', '30', '30', '40', '40', '50', '50'
Expected: Highest score: 50; Average time: 30 minutes; correct ID and all records saved. Invalid inputs rejected and re-entered. 

Test 5: Abnormal: invalid scores and times
Data: 'P05', '5', '-1', 'abc', '1.5', '10', '4', '61', '5.5', 'abc', '10', '20', '20', '30', '30', '40', '40', '50', '50'
Expected: Highest score: 50; Average time: 30 minutes; correct ID and all records saved. Invalid inputs rejected and re-entered. 

Test 6: Rounding: fractional average
Data: 'P06', '5', '1', '5', '1', '5', '2', '6', '2', '6', '2', '6'
Expected: Highest score: 2; Average time: 6 minutes; correct ID and all records saved. 

Test 7: File append. Run test 1 then test 3 in the same folder. Expected: both records retained.

Test 8: File error. Create a directory named player_scores.txt, then run test 1. Expected: statistics displayed and save error reported.