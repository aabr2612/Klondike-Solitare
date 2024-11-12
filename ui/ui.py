import os
import msvcrt

# Header of the game
def header():
    os.system("cls")
    print("""
            #   # #      ###  #   # ####  ### #   # #####    #####   ###  #     ### #####   ###   ### ####   #####
            #  #  #     #   # ##  # #   #  #  #  #  #       ##      #   # #      #    #    ## ##   #  #   #  #    
            ###   #     #   # # # # #   #  #  ###   ####     #####  #   # #      #    #   #######  #  ####   #### 
            #  #  #     #   # #  ## #   #  #  #  #  #            ## #   # #      #    #   ##   ##  #  #   #  #    
            #   # #####  ###  #   # ####  ### #   # #####    #####   ###  ##### ###   #   ##   ## ### #    # #####
            """)
    
# Main menu
def main_menu():
    header()
    print("""
                                                    1. Play Game
                                                    2. Instructions
                                                    3. Exit
            """)
    option = input("                                                    Enter your choice: ")
    return option

# Instructions for playing the game
def instructions_to_play_game():
    header()
    print("\n                                                    How to play game")
    print("""
            1. To draw a card from the stock pile enter 1.
            2. To move a single card enter 2 and input the source pile and destination pile. (T -> Tableau, 'F' -> Foundations and 'W' -> Waste
            3. Select the indexes of the source and destination. In case of waste pile index not required.
            4. To move multiple cards enter 3. Enter the indexes of source and destination tableau. Enter the card name to move.""")
    print("\n                                                    Rules and instructions")
    print("""
            1. Card move to tableau:
                --> While moving card from waste, tableau or foundation to tableau the suit of cards must be different.
                --> The rank of source card to move must be one smaller than the destination card.
                
            2. Card move to foundation:
                --> While moving card from waste or tableau to foundation the suit must be same.
                --> The rank of source card must be one larger then the destination card.
            
            3. Multiple card movement:
                --> While moving multiple cards, to select a card enter it's small name as for King of Diamonds [13D] we have 13D.
                --> Same destination indexes must not be selected or move will not be made.
                   
            4. Win condition:
                --> All the four foundation piles must have 13 cards of same suit in order to win the game.
            """)
    print("\n                                                    Press any key to continue...",end="")
    msvcrt.getch()

# Game play menu for making actions
def game_menu():
    print("""
          1. Draw card from stock pile
          2. Move card
          3. Move multiple cards
          4. Get Hint
          5. Exit""")
    option = input("          Enter your choice: ")
    return option

# Game won
def game_won(count,hint):
    os.system("cls")
    header()
    print(f"\n               Congratulations! You completed the game in {count} moves and used {hint} hints. Press any key to continue...",end="")
    msvcrt.getch()
    