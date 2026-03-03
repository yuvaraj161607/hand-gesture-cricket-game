import random

     
def game_engine(target=None):
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
        batter_gesture= random.randint(0,10)
        batter_list.append(batter_gesture)

        #analyze bowler gesture
        bowler_gesture=random.randint(0,10)
        bowler_list.append(bowler_gesture)

        #balls counter
        number_of_balls+=1

        #if batter_gesture==bowler_gesture print(out) break
        if(bowler_gesture == batter_gesture):
            break
        #else batter_score+= batter_gesture
        else:
            batter_score+=batter_gesture
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