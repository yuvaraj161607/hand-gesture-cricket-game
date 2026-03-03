import random
def toss(player1, player2):
    players=[player1,player2]
    toss_winner=random.choice(players)
    print(toss_winner," have won the toss.")
    choice1=int(input("Enter your choice to play (press any odd number for bat) : "))
    if (choice1 in (1,3,5,7,9)):
        batter=toss_winner
        if (toss_winner == player1):
            bowler = player2
        else :
            bowler= player1
    else:
        bowler=toss_winner
        if(toss_winner==player1):
            batter=player2
        else:
            batter=player1
    print("Batter: ",batter)
    print("Bowler: ",bowler)
    return batter,bowler