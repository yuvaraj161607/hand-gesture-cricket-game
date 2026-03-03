from play_match import play_match
from play_one_player import play_one_player
def main_menu():
    print("1.One Player")
    print("2.Second Player")
    choice=input("Enter Your Choice")
    if (choice == "2"):
        play_match()
    elif (choice == "1"):
        play_one_player()
    else:
        print("Invalid Choice")

if __name__=="__main__":
    main_menu()