from toss import toss
from game_engine import game_engine, print_scoreboard

def play_one_player():
    Computer = "Computer"
    player2 = input("Enter Player name: ")

    # TOSS
    first_batter, first_bowler = toss(Computer, player2)

    # FIRST INNINGS
    print("\n--- FIRST INNINGS ---")
    if first_batter == player2:
        score1,balls1,list1,list2,result1 = game_engine(mode="single", batter="player")
    else:
        score1,balls1,list1,list2,result1 = game_engine(mode="single", batter="computer")

    target = score1 + 1
    print_scoreboard(first_batter, score1, balls1, list1, list2)
    print(f"Target for {first_bowler}: {target}")

    second_batter = first_bowler
    second_bowler = first_batter

    # SECOND INNINGS
    print("\n--- SECOND INNINGS ---")
    if second_batter == Computer:
        score2,balls2,list3,list4,result2 = game_engine(target, mode="single", batter="computer")
    else:
        score2,balls2,list3,list4,result2 = game_engine(target, mode="single", batter="player")

    print_scoreboard(second_batter, score2, balls2, list3, list4)

    # FINAL RESULT
    if result2 is True:
        print(f"{second_batter} Wins!")
    elif result2 is False:
        print(f"{first_batter} Wins!")
    else:
        print("TIE!")

"""from toss import toss
from game_engine import game_engine

def play_one_player():
    Computer = "Computer"
    player2 = input("Enter Player name: ")

    # TOSS
    first_batter, first_bowler = toss(Computer, player2)

    # FIRST INNINGS
    print("\n--- FIRST INNINGS ---")
    if first_batter == player2:
        score1,balls1,list1,list2,result1 = game_engine(mode="single", batter="player")
    else:
        score1,balls1,list1,list2,result1 = game_engine(mode="single", batter="computer")

    target = score1 + 1
    print(f"\n{first_batter} scored {score1} in {balls1} balls")
    print(f"Target for {first_bowler}: {target}")

    second_batter = first_bowler
    second_bowler = first_batter

    # SECOND INNINGS
    print("\n--- SECOND INNINGS ---")
    if second_batter == Computer:
        score2,balls2,list3,list4,result2 = game_engine(target, mode="single", batter="computer")
    else:
        score2,balls2,list3,list4,result2 = game_engine(target, mode="single", batter="player")

    print(f"\n{second_batter} scored {score2} in {balls2} balls")

    # RESULT
    if result2 is True:
        print(f"\n🏆 {second_batter} wins!")
    elif result2 is False:
        print(f"\n🏆 {first_batter} wins!")
    else:
        print("\n🤝 It's a Tie!")
"""

"""
from toss import toss
from game_engine import game_engine

def play_one_player():
    Computer = "Computer"
    player2 = input("Enter Player name: ")
    mode = "single"

    # TOSS
    first_batter, first_bowler = toss(Computer, player2)

    # FIRST INNINGS
    print("\n--- FIRST INNINGS ---")
    if first_batter == player2:
        score1,balls1,list1,list2,result1 = game_engine(mode="single", batter="player")
    else:
        score1,balls1,list1,list2,result1 = game_engine(mode="single", batter="computer")

    target = score1 + 1
    print(f"{first_batter} scored {score1}({balls1})")

    second_batter = first_bowler
    second_bowler = first_batter

    # SECOND INNINGS
    print("\n--- SECOND INNINGS ---")
    print(f"Target: {target}")
    if second_batter == Computer:
        score2,balls2,list3,list4,result2 = game_engine(target, mode="single", batter="computer")  # fix here
    else:
        score2,balls2,list3,list4,result2 = game_engine(target, mode="single", batter="player")    # fix here

    print(f"{second_batter} scored {score2}({balls2})")

    # RESULT
    if result2:
        print(f"\n🏆 {second_batter} is the winner!")
    elif result2 == False:
        print(f"\n🏆 {first_batter} is the winner!")
    else:
        print("\n🤝 It's a Tie!")
        """