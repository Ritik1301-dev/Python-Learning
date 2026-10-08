import random 

def play_game():
    lucky_num = random.randint(1,50)

    while True:
        user_num = int(input("Guess the lucky num: "))

        if user_num == lucky_num : 
            print("You won the game..")
            break
        elif user_num < lucky_num:
            print("Too Low")
        else: print("Too High")
    print("Thanx for playing the game.")
        
play_game ()

