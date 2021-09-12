import os
import random
import time

HOME = 100
TOTAL_DICE_NUMBER = 6
clear = lambda: os.system('cls')

#TODO : Add a beautiful intro page... research for animation if possible otherwise heading like structure for console.
#TODO : Once completed. Merge this file to main.py and remove this file completely.



snakes = {
    "27" : "5",
    "40" : "3",
    "43" : "18", 
    "54" : "31",
    "66" : "45",
    "76" : "58",
    "89" : "53",
    "99" : "41"
}

ladders = {
    "4" : "25",
    "13" : "46",
    "33" : "49",
    "42" : "63",
    "50" : "69",
    "62" : "81",
    "74" : "92"
}

def continue_game():
    user_choice = input('''
    Press 0 to go back to main menu
    Type 'Exit' to exit the game.
        ''')
    if user_choice == '0':
        main_menu()
    elif user_choice.lower() == 'exit':
        exit()

def dots():
    dices = "🎲🎲🎲🎲🎲"
    for i in range(len(dices)):
        print(dices[i],sep="", end="", flush=True)
        time.sleep(0.3)
    print()

def get_dice_face():
    clear()
    print("Rolling the dice", end="")
    dots()
    dice_face = random.randint(1,TOTAL_DICE_NUMBER)
    print(f"The dice shows {dice_face}")
    return dice_face


def get_players():
    player1 = input("Enter name of Player 1 : ")
    player2 = input("Enter name of Player 2 : ")
    print(f"{player1} is up against {player2}")
    clear()
    return player1, player2



def check_win(player_name, player_pos):
    if player_pos == HOME:
        print(f"Congrats! {player_name} won!🎊🎉🎇")
        exit()
    elif player_pos > HOME:
        print("Exceeded")



def final_player_pos(player_pos, dice_face):
    if (player_pos + dice_face) > HOME:
        print(f"You need {HOME - player_pos} steps to win")
    else:
        player_pos = player_pos + dice_face
    return player_pos


#TODO 1: clearing before running to item.. probably through adding these lines to a function
#TODO 2: Make this function availabel for multiple users
#TODO 3 Refactor the code and remove unnecessary lines.. add useful comments.
def start_game():
    clear()
    player1_name, player2_name = get_players()
    player1_pos = 0
    player2_pos = 0 

    while True:
        go = input(f'{player1_name}: Please press "Enter" to roll the dice')
        dice_face = get_dice_face()
        player1_pos = final_player_pos(player1_pos, dice_face)
        print(f"{player1_name}: Now.. You are {HOME - player1_pos} steps away from HOME!")
        # clear()

        check_win(player1_name, player1_pos)

        go = input(f'{player2_name}: Please press "Enter" to roll the dice')
        dice_face = get_dice_face()
        player1_pos = player1_pos + dice_face
        print(f"{player2_name}: Now.. You are {HOME - player1_pos} steps away from HOME!")
        # clear()

        check_win(player2_name, player2_pos)


def rules():
    clear()
    print('''
    1. When a piece comes on a number which lies on the top of a snake (face of the snake), 
        then the piece/token will land below to the bottom of the snake (tail of it) that can also be said as an unlucky move.

    2. If somehow the piece falls on the ladder base, 
        it will immediately climb to the top of the ladder (which is considered to be a lucky move).
    
    3. Whereas if a player lands on the bottom of the snake or top of a ladder, 
        the player will remain in the same spot (same number) and will not get affected by any particular rule. The players can never move down ladders.
    
    4. The pieces of different players can overlap each other without knocking out anyone. 
        There is no concept of knocking out by opponent players in Snakes and Ladders.
    
    5. To win, the player needs to roll the exact number of die to land on the number 100. 
        If he/she fails to do so, then the player needs to roll the die again in the next turn. 
        For example, if a player is on the number 98 and the die roll shows the number 4, 
        then the player cannot move its piece until he/she gets a 2 to win or 1 to be on the 99th number.
    ''')
    continue_game()
    

def how_to_play():
    clear()
    print('''
    1. Each player puts their name and tha game starts.
    
    2. Take it in turns to roll the dice. Counter automatically moves forward the number of spaces shown on the dice.
    
    3. If your counter lands at the bottom of a ladder, you can move up to the top of the ladder.
    
    4. If your counter lands on the head of a snake, you must slide down to the bottom of the snake.
    
    5. The first player to get to the space that says 'home' is the winner.
    ''')
    continue_game()

#TODO : find a way to map index value to dictionary item and then change it
def change_snake_pos():
    clear()
    print('''
        Snake Mouth     Snake Tail''')
    for key,val  in snakes.items():
        print(f'''
        {key}               {val}
        ''')
    snake_mouth_old = input("Enter the snake mouth and snake tail (seperated by ',') your want to change? ")
    snake_mouth_new, snake_tail_new = input("Enter the new values for mouth and tail (seperated by ',') that you want to change? ").split(',')
    snakes.pop(snake_mouth_old)
    snakes[snake_mouth_new] = snake_tail_new
    print('''
        Snake Mouth     Snake Tail''')
    for key,val  in snakes.items():
        print(f'''
        {key}               {val}
        ''')
    continue_game()
        

#TODO : create this function in the same way as change_snake_pos() function
def change_ladder_pos():
    clear()
    print('''
        Ladder Bottom     Ladder Top''')
    for key,val  in ladders.items():
        print(f'''
        {key}               {val}
        ''')
    ladder_bottom_old = input("Enter the Ladder bottom value you want to change? ")
    ladder_bottom_new, ladder_top_new = input("Enter the new values for bottom and top (seperated by ',') that you want to change? ").split(',')
    ladders.pop(ladder_bottom_old)
    ladders[ladder_bottom_new] = ladder_top_new
    print('''
        Ladder Bottom     Ladder Top''')
    for key,val  in ladders.items():
        print(f'''
        {key}               {val}
        ''')
    continue_game()
        
    

def settings():
    clear()
    while True:
        setting_input = input(f''' 
        Press 1 - Change Snakes Position
        Press 2 - Change Ladder Position
        Enter your choice - \
        ''')
        if setting_input == "1":
            change_snake_pos()
        elif setting_input == "2":
            change_ladder_pos()
        else:
            input("\n\tWrong input. Please Try Again!")
            clear()
            continue



def main_menu_options(choice):
    if choice ==  1:
        start_game()
    elif choice == 2:
        rules()
    elif choice == 3:
        how_to_play()
    elif choice == 4:
        settings()
    elif choice == 5:
        clear()
        exit()


def main_menu():
    clear()
    choice = int(input('''
    Welcome to the Snakes🐍 and Ladder Game!
        
        Press 1 - Start the game ▶
        Press 2 - Rules📕
        Press 3 - How to Play ❓ 
        Press 4 - Settings⚙
        Press 5 - Exit🚪
        Enter your choice - \
    '''))
    main_menu_options(choice)


if __name__== '__main__':
    main_menu()