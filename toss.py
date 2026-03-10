import random

def toss(player1, player2):
    players = [player1, player2]
    toss_winner = random.choice(players)
    print(toss_winner, "have won the toss.")

    if toss_winner == "Computer":
        choice = random.choice(["bat", "bowl"])
        print("Computer Chooses: ", choice)
    else:
        choice = input("Press bat or bowl : ").strip().lower()

    if choice == "bat":
        batter = toss_winner
        bowler = player2 if toss_winner == player1 else player1
    else:
        bowler = toss_winner
        batter = player2 if toss_winner == player1 else player1

    print("Batter:", batter)
    print("Bowler:", bowler)
    return batter, bowler