FUNCTION ReadInteger(prompt, minimum, maximum)
    REPEAT
        INPUT value using prompt
        IF value is an integer AND value >= minimum AND
           (maximum is NONE OR value <= maximum) THEN
            RETURN value as integer
        ENDIF
        OUTPUT "Invalid whole number or range"
    UNTIL valid
ENDFUNCTION

START
    REPEAT
        INPUT playerID
        REMOVE surrounding spaces
    UNTIL playerID is not empty
    games = ReadInteger("Games", 5, 10)
    records = empty list
    FOR game = 1 TO games
        score = ReadInteger("Score", 0, NONE)
        minutes = ReadInteger("Minutes", 5, 60)
        APPEND (score, minutes) TO records
    NEXT game
    highest = MAXIMUM score in records
    total = SUM minutes in records
    average = (2 * total + games) DIV (2 * games)
    OUTPUT playerID, highest, average
    TRY
        OPEN player_scores.txt in append mode
        WRITE playerID, games, each score and minutes,
              highest and average
        CLOSE file
        OUTPUT "Record saved"
    IF file error THEN
        OUTPUT "Could not save record"
    ENDTRY
END