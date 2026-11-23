# Games club score recording system
# Python 3.4 or later; no external packages required.
def read_integer(prompt, minimum, maximum=None):
    """Repeat until a whole number in the permitted range is entered."""
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum and (maximum is None or value <= maximum):
                return value
        except ValueError:
            pass
        print("Invalid whole number or range. Try again.")


def main():
    print("Games club score recorder")
    player_id = input("Player ID: ").strip()
    while not player_id:
        print("Player ID cannot be blank.")
        player_id = input("Player ID: ").strip()
    games = read_integer("Number of games (5-10): ", 5, 10)
    records = []
    for game in range(1, games + 1):
        print("Game {}".format(game))
        score = read_integer("Score (0 or more): ", 0)
        minutes = read_integer("Time (5-60 whole minutes): ", 5, 60)
        records.append((score, minutes))

    # Calculate statistics from the list of score/time pairs.
    highest = max(score for score, minutes in records)
    total = sum(minutes for score, minutes in records)
    # Integer arithmetic rounds to nearest minute, with halves rounded up.
    average = (2 * total + games) // (2 * games)
    summary = "Player ID: {}\nHighest score: {}\nAverage time: {} minutes".format(
        player_id, highest, average)
    print(summary)

    # Append rather than overwrite previous player records.
    try:
        with open("player_scores.txt", "a", encoding="utf-8") as file:
            file.write(summary + "\nNumber of games: {}\n".format(games))
            for game, (score, minutes) in enumerate(records, 1):
                file.write("Game {}: score {}, time {} minutes\n".format(
                    game, score, minutes))
            file.write("---\n")
        print("Record saved to player_scores.txt")
    except OSError:
        print("Could not save record to player_scores.txt")


if __name__ == "__main__":
    main()
