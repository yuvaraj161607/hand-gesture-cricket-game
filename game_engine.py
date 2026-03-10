import random
from score_calculator import get_player_gesture, close_camera

def play_sound(event):
    try:
        import winsound
        if event == "out":
            winsound.Beep(300, 500)
        elif event == "runs":
            winsound.Beep(800, 150)
        elif event == "win":
            winsound.Beep(1000, 200)
            winsound.Beep(1200, 400)
    except:
        pass

def print_scoreboard(name, score, balls, batter_list, bowler_list):
    print("\n" + "-"*40)
    print(f"  INNINGS SUMMARY — {name}")
    print("-"*40)
    print(f"  Total Score : {score}")
    print(f"  Balls Faced : {balls}")
    if balls > 0:
        print(f"  Strike Rate : {round((score/balls)*100, 1)}")
    print(f"  Ball-by-Ball: {batter_list}")
    print(f"  Bowler List : {bowler_list}")
    print("-"*40)

def game_engine(target=None, mode="single", batter="player",
                p1_name="Player", p2_name="Computer"):
    result = None
    batter_score = 0
    number_of_balls = 0
    batter_list = []
    bowler_list = []

    while True:
        batter_gesture = None
        bowler_gesture = None

        if mode == "single":
            if batter == "player":
                # player bats, computer bowls
                batter_gesture = get_player_gesture(
                    score=batter_score,
                    balls=number_of_balls,
                    target=target,
                    label="You are batting — show fingers & SPACE"
                )
                if batter_gesture is None:
                    close_camera()
                    break
                bowler_gesture = random.randint(1, 10)

            else:
                # computer bats, player bowls
                batter_gesture = random.randint(1, 10)
                bowler_gesture = get_player_gesture(
                    score=batter_score,
                    balls=number_of_balls,
                    target=target,
                    label="You are bowling — show fingers & SPACE"
                )
                if bowler_gesture is None:
                    close_camera()
                    break

        # count ball
        number_of_balls += 1
        batter_list.append(batter_gesture)
        bowler_list.append(bowler_gesture)

        print(f"Ball {number_of_balls}: Batter {batter_gesture} | Bowler {bowler_gesture}", end="  ->  ")

        # OUT check
        if bowler_gesture == batter_gesture:
            print("OUT!")
            play_sound("out")
            break

        # add runs
        batter_score += batter_gesture
        print(f"{batter_gesture} runs | Total: {batter_score}")
        play_sound("runs")

        # target check
        if target is not None and batter_score >= target:
            print("Target reached!")
            play_sound("win")
            break

    # close camera at end of innings
    close_camera()

    # result
    if target is None:
        result = None
    elif batter_score >= target:
        result = True
    else:
        result = False

    return batter_score, number_of_balls, batter_list, bowler_list, result
"""
        else:

            batter_gesture, bowler_gesture = get_both_gestures(
                score=batter_score,
                balls=number_of_balls,
                target=target,
                player1_name=p1_name,
                player2_name=p2_name
            )
            if batter_gesture is None or bowler_gesture is None:
                close_camera()
                break

        # count ball
        number_of_balls += 1
        batter_list.append(batter_gesture)
        bowler_list.append(bowler_gesture)

        print(f"Ball {number_of_balls}: Batter {batter_gesture} | Bowler {bowler_gesture}", end="  →  ")

        # OUT check
        if bowler_gesture == batter_gesture:
            print("OUT!")
            play_sound("out")
            break

        # add runs
        batter_score += batter_gesture
        print(f"{batter_gesture} runs | Total: {batter_score} 🟢")
        play_sound("runs")

        # target check
        if target is not None and batter_score >= target:
            print("Target reached! ")
            play_sound("win")
            break

    close_camera()

    if target is None:
        result = None
    elif batter_score >= target:
        result = True
    else:
        result = False

    return batter_score, number_of_balls, batter_list, bowler_list, result


"""

"""import random
from score_calculator import get_player_gesture, close_camera

# sound effects
def play_sound(event):
    try:
        import winsound
        if event == "out":
            winsound.Beep(300, 500)    # low beep = OUT
        elif event == "runs":
            winsound.Beep(800, 150)    # high beep = runs scored
        elif event == "win":
            winsound.Beep(1000, 200)
            winsound.Beep(1200, 400)
    except:
        pass   # if winsound not available, silently skip

def print_scoreboard(name, score, balls, batter_list, bowler_list):
    print("\n" + "="*40)
    print(f"  📊 INNINGS SUMMARY — {name}")
    print("="*40)
    print(f"  Total Score : {score}")
    print(f"  Balls Faced : {balls}")
    if balls > 0:
        print(f"  Strike Rate : {round((score/balls)*100, 1)}")
    print(f"  Ball-by-Ball: {batter_list}")
    print(f"  Bowler List : {bowler_list}")
    print("="*40)

def game_engine(target=None, mode="single", batter="player"):
    result = None
    batter_score = 0
    number_of_balls = 0
    batter_list = []
    bowler_list = []

    while True:
        batter_gesture = None
        bowler_gesture = None

        if mode == "single":
            if batter == "player":
                # player bats — camera stays open
                batter_gesture = get_player_gesture(
                    score=batter_score,
                    balls=number_of_balls,
                    target=target,
                    label="YOU are batting — show fingers & press SPACE"
                )
                if batter_gesture is None:
                    close_camera()
                    break
                bowler_gesture = random.randint(1, 10)

            else:
                # computer bats, player bowls
                batter_gesture = random.randint(1, 10)
                bowler_gesture = get_player_gesture(
                    score=batter_score,
                    balls=number_of_balls,
                    target=target,
                    label="YOU are bowling — show fingers & press SPACE"
                )
                if bowler_gesture is None:
                    close_camera()
                    break

        else:
            # multi mode — both players use camera
            batter_gesture = get_player_gesture(
                score=batter_score,
                balls=number_of_balls,
                target=target,
                label="BATTER — show fingers & press SPACE"
            )
            if batter_gesture is None:
                close_camera()
                break

            bowler_gesture = get_player_gesture(
                score=batter_score,
                balls=number_of_balls,
                target=target,
                label="BOWLER — show fingers & press SPACE"
            )
            if bowler_gesture is None:
                close_camera()
                break

        # count ball
        number_of_balls += 1
        batter_list.append(batter_gesture)
        bowler_list.append(bowler_gesture)

        print(f"Ball {number_of_balls}: Batter {batter_gesture} | Bowler {bowler_gesture}", end="  →  ")

        # OUT check
        if bowler_gesture == batter_gesture:
            print("OUT! 🔴")
            play_sound("out")
            break

        # add runs
        batter_score += batter_gesture
        print(f"{batter_gesture} runs | Total: {batter_score} 🟢")
        play_sound("runs")

        # target check
        if target is not None and batter_score >= target:
            print("Target reached! ✅")
            play_sound("win")
            break

    # close camera at end of innings
    close_camera()

    # result
    if target is None:
        result = None
    elif batter_score >= target:
        result = True
    else:
        result = False

    return batter_score, number_of_balls, batter_list, bowler_list, result
"""

"""import random
from score_calculator import get_player_gesture

def game_engine(target=None, mode="single", batter="player"):
    result = None
    batter_score = 0
    number_of_balls = 0
    batter_list = []
    bowler_list = []

    while True:
        batter_gesture = None
        bowler_gesture = None

        if mode == "single":
            if batter == "player":
                # player bats, computer bowls
                batter_gesture = get_player_gesture()
                if batter_gesture is None:
                    continue
                bowler_gesture = random.randint(1, 6)

            else:
                # computer bats, player bowls
                batter_gesture = random.randint(1, 6)
                bowler_gesture = get_player_gesture()
                if bowler_gesture is None:
                    continue

        else:
            # multi mode — both players use camera
            print("Player 1 (Batter) — show your gesture")
            batter_gesture = get_player_gesture()
            if batter_gesture is None:
                continue

            print("Player 2 (Bowler) — show your gesture")
            bowler_gesture = get_player_gesture()
            if bowler_gesture is None:
                continue

        # count the ball
        number_of_balls += 1
        batter_list.append(batter_gesture)
        bowler_list.append(bowler_gesture)

        print(f"Batter: {batter_gesture}  |  Bowler: {bowler_gesture}")

        # OUT check
        if bowler_gesture == batter_gesture:
            print("OUT!")
            break

        # add runs
        batter_score += batter_gesture
        print(f"Runs this ball: {batter_gesture}  |  Total: {batter_score}")
        print("---------------")

        # target check
        if target is not None and batter_score >= target:
            break

    # result — outside while loop, correct indentation
    if target is None:
        result = None
    elif batter_score >= target:
        result = True
    else:
        result = False

    return batter_score, number_of_balls, batter_list, bowler_list, result
"""




"""
import random
from score_calculator import get_player_gesture
def game_engine(target=None,mode="single",batter="player"):
    result= None
    batter_score=0
    number_of_balls=0
    batter_list=[]
    bowler_list=[]
    #while loop 
    while True:
        #analyze batter gesture
        #if batter_mode == "user" :
        #     batter_gesture
        #else:
        if mode == "single" :
            if batter == "player":
                batter_gesture= get_player_gesture()
                print("Player Gesture: ",batter_gesture)
                if batter_gesture is None:
                    continue
                batter_list.append(batter_gesture)

        #analyze bowler gesture
                bowler_gesture=random.randint(1,6)
                print("Computer Gesture: ",bowler_gesture)
                bowler_list.append(bowler_gesture)
            else:
                batter_gesture= random.randint(1,6)
                print("Computer Gesture: ",batter_gesture)
                if batter_gesture is None:
                    continue
                batter_list.append(batter_gesture)

                bowler_gesture=get_player_gesture()
                print("Player Gesture: ",bowler_gesture)
                bowler_list.append(bowler_gesture)


                 
        else:
            
            batter_gesture= get_player_gesture()
            print("Player Gesture: ",batter_gesture)
            batter_list.append(batter_gesture)

        #analyze bowler gesture
            bowler_gesture=get_player_gesture()
            print("Computer Gesture: ",bowler_gesture)
            bowler_list.append(bowler_gesture)

        #balls counter
        number_of_balls+=1

        #if batter_gesture==bowler_gesture print(out) break
        if(bowler_gesture == batter_gesture):
            print("OUT!")
            break
        #else batter_score+= batter_gesture
        else:
            batter_score+=batter_gesture
            #print("Runs Scored: ",batter_gesture)
            print("Total Score ",batter_score)
            print("---------------")
            if target is not None:
                if batter_score>=target:
                    break
    if target is None:
                result = None
    else:
        if batter_score>=target:
            result= True
        else:
            result = False
    return batter_score,number_of_balls,batter_list,bowler_list, result
    """