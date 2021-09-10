import os
clear = lambda: os.system('cls')

def start_game():
    player1 = input("Enter name of Player 1 : ")
    player2 = input("Enter name of Player 2 : ")

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
            For example, if a player is on the number 98 and the die roll shows the number 4, then the player cannot move its piece until he/she gets a 2 to win or 1 to be on the 99th number.
    ''')
    user_choice = input('''
            Press 0 to go back to main main menu
            Type 'Exit' to exit the game.
        ''')
    if user_choice == '0':
        main_menu()
    elif user_choice.lower() == 'exit':
        exit()

def how_to_play():
    pass

def settings():
    pass



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
    '''))
    main_menu_options(choice)


main_menu()
if __name__== '__main__':
    print("Hello, User!")