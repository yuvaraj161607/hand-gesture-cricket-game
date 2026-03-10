from two_players import play_match
from play_one_player import play_one_player

def main_menu():
    while True:
        print("\n1. One Player")
        print("2. Two Players")
        print("3. Exit")
        print("Currently, Two Players mode is not available! \n Kindly Select One Player Mode by pressing '1' \n")
        choice = input("Enter Your Choice: ").strip().lower()

        #if choice == "2":
        #    play_match()
        if choice == "1":
            play_one_player()
        elif choice == "3":
            break
        else:
            print("Invalid Choice. Enter 1, 2 or 3.")

if __name__ == "__main__":
    main_menu()