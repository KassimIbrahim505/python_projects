def word_value(word):
    total = 0

    for char in word:
        value = ord(char.upper()) - ord('A') + 1
        if char.isupper():
            value *= 2
        total += value
    return total

def battle(our_team, opponent_team):
    our_wins = 0
    their_wins = 0

    for ours, theirs in zip(our_team.split(), opponent_team.split()):
        our_score = word_value(ours)
        their_score = word_value(theirs)

        if our_score > their_score:
            our_wins += 1
        elif their_score > our_score:
            their_wins += 1

    if our_wins > their_wins:
        return "We win!"
    if our_wins < their_wins:
        return "We lose!"
    return "It's a tie!"
help(zip)

print(battle("Hello World", "hello world"))  # Example usage