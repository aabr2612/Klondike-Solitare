from game_files.game import Game
import os
import ui.ui
import msvcrt
from time import sleep

# Main
def main():
      # Main loop of the menu
      while(True):
            # Menu choice
            os.system("cls")
            menu_choice = ui.ui.main_menu()

            # If 1 the game starts
            if menu_choice == "1":
                  # Game object
                  game = Game()
                  game_condition = "F"
                  
                  # Main game loop
                  while(True):
                        os.system("cls")
                        ui.ui.header()
                        game.display()

                        # If wins the game
                        game_condition = game.game_win_condition()
                        if(game_condition=="W"):
                            ui.ui.game_won(game.count,game.hint_count)
                            break

                        elif(game_condition=="F"):
                            
                            # Game move choice
                            game_choice = ui.ui.game_menu()
                            
                            # If choice is 1 draw card from stockpile
                            if game_choice=="1":
                                game.draw_card_from_stockpile()
                                
                            # If choice is 2 move card
                            elif game_choice=="2":
                                source = input("          Enter the source(Tableau [T], Waste[W], Foundation[F]): ")
                                destination = input("          Enter the destination(Tableau [T], Foundation[F]): ")
                                source_index = 8
                                if source.capitalize()=="T" or source.capitalize()=="F":
                                    source_index = input("          Enter the source index: ")
                                destination_index = input("          Enter the destination index: ")
                                msg = game.move_card(source,destination,source_index,destination_index)
                                print("          "+msg)
                                sleep(0.3)
                                
                            # If choice is 3 move multiple cards
                            elif game_choice=="3":
                                source_index = input("          Enter the source tableau index: ")
                                destination_index = input("          Enter the destination tableau index: ")
                                card_name = input("          Enter card name from source as 'AC', 'KD': ")
                                msg = game.move_multiple_cards(source_index,destination_index,card_name)
                                print("          "+msg)
                                sleep(0.3)

                            # If choice is 4 get hint
                            elif game_choice=="4":
                                print("          "+game.get_hint())
                                sleep(2)

                            # If choice is 5 return to main menu
                            elif game_choice=="5":
                                break
                            
                            # Invalid input
                            else:
                                print("          Invalid choice!")
                                sleep(0.3)
                        elif (game_condition=="C"):
                            sleep(0.7)

            # Displaying instructions
            elif menu_choice=="2":
                os.system("cls")
                ui.ui.instructions_to_play_game()
                  
            # Exit the game
            elif menu_choice=="3":
                  print("                                                    Thanks for playing the game!")
                  sleep(1)
                  os.system("cls")
                  break
            
            # Invalid input
            else:
                  print("                                                    Invalid choice!")
                  sleep(1)

# Calling main        
if __name__ == "__main__":
    main()