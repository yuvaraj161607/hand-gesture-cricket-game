from toss import toss
from game_engine import game_engine
def play_one_player():
    Computer = "Computer"
    player2 = input("Enter Player two name: ")
    mode="random"
    first_batter,first_bowler=toss(Computer,player2)
    score1,balls1,list1,list2,result1=game_engine()
    target=score1+1
    print(f"{first_batter} scored {score1} and faced {balls1}")
    second_batter=first_bowler
    second_bowler=first_batter
    score2,balls2,list3,list4,result2=game_engine(target)
    print(f"{second_batter} scored {score2} and faced {balls2}")
    if result2:
        print(f"{second_batter} is the winner")
    else :
        print(f"{first_batter} is the winner")

    """
    elif (result2 == result1):
        print("Tie")
    """
    