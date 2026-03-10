from toss import toss
from game_engine import game_engine, print_scoreboard

def play_match():
    player1 = input("Enter Player one name: ")
    player2 = input("Enter Player two name: ")

    first_batter, first_bowler = toss(player1, player2)

    # FIRST INNINGS
    print("\n--- FIRST INNINGS ---")
    score1,balls1,list1,list2,result1 = game_engine(
        mode="multi",
        p1_name=first_batter,
        p2_name=first_bowler
    )

    target = score1 + 1
    print_scoreboard(first_batter, score1, balls1, list1, list2)
    print(f"Target for {first_bowler}: {target}")

    second_batter = first_bowler
    second_bowler = first_batter

    # SECOND INNINGS
    print("\n--- SECOND INNINGS ---")
    score2,balls2,list3,list4,result2 = game_engine(
        target,
        mode="multi",
        p1_name=second_batter,
        p2_name=second_bowler
    )
    print_scoreboard(second_batter, score2, balls2, list3, list4)

    # FINAL RESULT
    if score2 > score1:
        print(f"{second_batter} WINS!")
    elif score2 < score1:
        print(f"{first_batter} WINS!")
    else:
        print("TIE!")