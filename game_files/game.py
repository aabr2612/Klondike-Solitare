from classes.stack import Stack
from classes.deck import Deck
from classes.queue import Queue
from classes.card import Card
import game_files.utility


# Game Class
class Game:
    # Constructor
    def __init__(self):
        self.tableau=[Stack() for _ in range(7)] # Initializing tableau
        self.foundation=[Stack() for _ in range(4)] # Initalizing foundations
        self.deck = Deck() # Initializing deck
        self.stock_pile = Queue() # Stock pile
        self.initialize_game() # Initializing game
        self.count = 0 # Count to keep a track of the moves
        self.hint_count = 0 # Setting the hint count to 0
    
    # Game initialization
    def initialize_game(self):
        # Pushing cards into tableau
        for i in range(7):
            for j in range(i+1):
                card = self.deck.draw_card()
                if card:
                    if j==i:
                        card.flip_card()
                    self.tableau[i].push(card)
        
        card = self.deck.draw_card()
        
        # Pushing cards into stockpile from deck
        while card:
            self.stock_pile.enqueue(card)
            card=self.deck.draw_card()

    # Move card functionality
    def move_card(self,source,destination,source_index,destination_index):
        try:
            # Capitalizing the source and destination keywords to ensure valid comparison
            source = source.capitalize()
            destination = destination.capitalize()
            
            # Checks for source and destination movements and indexes
            if not game_files.utility.validate_movement(source,destination,source_index,destination_index):
                return "Invalid movements!"

            source_index = int(source_index)-1
            destination_index = int(destination_index)-1

            # If the card being moved is from tableau to tableau
            if source == "T" and destination=="T":
                # If the movement is valid
                if self.valid_tableau_to_tableau_move(source_index,destination_index):
                    msg = f"Card moved {str(self.tableau[source_index].peek())} ---> {str(self.tableau[destination_index].peek())}"
                    self.tableau[destination_index].push(self.tableau[source_index].pop())
                    self.count+=1
                    return msg

            # If the card being moved is from tableau to foundation
            if source == "T" and destination=="F":
                # If the movement is valid
                if self.valid_tableau_to_foundation_move(source_index,destination_index):
                    msg = f"Card moved {str(self.tableau[source_index].peek())} ---> {str(self.foundation[destination_index].peek())}"
                    self.foundation[destination_index].push(self.tableau[source_index].pop())
                    self.count+=1
                    return msg
        
            # If the card being moved is from foundation to tableau
            if source == "F" and destination=="T":
                # If the movement is valid
                if self.valid_foundation_to_tableau_move(source_index,destination_index):
                    msg = f"Card moved {str(self.foundation[source_index].peek())} ---> {str(self.tableau[destination_index].peek())}"
                    self.tableau[destination_index].push(self.foundation[source_index].pop())
                    self.count+=1
                    return msg

            # If the card being moved is from waste to tableau
            if source == "W" and destination=="T":
                # If the movement is valid
                if self.valid_waste_to_tableau_move(destination_index):
                    msg = f"Card moved {str(self.stock_pile.peek())} ---> {str(self.tableau[destination_index].peek())}"
                    self.tableau[destination_index].push(self.stock_pile.dequeue())
                    self.count+=1
                    return msg
                    
            # If the card being moved is from waste to foundation
            if source == "W" and destination=="F":
                # If the movement is valid
                if self.valid_waste_to_foundation_move(destination_index):
                    msg = f"Card moved {str(self.stock_pile.peek())} ---> {str(self.foundation[destination_index].peek())}"
                    self.foundation[destination_index].push(self.stock_pile.dequeue())
                    self.count+=1
                    return msg
                
            # If no movement takes place returns invalid move
            return "Invalid move!"

        # If any error occurs
        except Exception as e:
            return f"Error occured: {e}"
    
    # Function to check the validity of the tableau to tableau movement
    def valid_tableau_to_tableau_move(self,source_index,destination_index):
        # If source is empty
        if self.tableau[source_index].is_empty():
            return False
        
        # Peek the cards of source and destination
        destination_card = self.tableau[destination_index].peek()
        source_card = self.tableau[source_index].peek()
        
        # If the destination tableau is empty and the source card being placed is King it is a valid move
        if (self.tableau[destination_index].is_empty() and source_card.get_rank()=="King"):
            return True

        # If the destination is empty and source card is not a king it is not a valid move
        if (self.tableau[destination_index].is_empty() and source_card.get_rank()!="King"):
            return False
        
        # If the source and destination both have cards then check the card's rank and color to ensure the movement
        if destination_card.check_rank_lower(source_card) and destination_card.check_card_color()!=source_card.check_card_color():
            return True
        
        # If none of the condition is valid it means the card movement is not valid
        return False
    
    # Function to check the validity of the tableau to foundation movement
    def valid_tableau_to_foundation_move(self,source_index,destination_index):
        # If source is empty
        if self.tableau[source_index].is_empty():
            return False

        # Peek the cards of source and destination
        destination_card = self.foundation[destination_index].peek()
        source_card = self.tableau[source_index].peek()

        # If the destination foundation is empty and the card being placed is Ace it is a valid move
        if (self.foundation[destination_index].is_empty() and source_card.get_rank()=="Ace"):
            return True

        # If the destination foundation is empty and source card is not an Ace it is not a valid move
        if (self.foundation[destination_index].is_empty() and source_card.get_rank()!="Ace"):
            return False
        
        # If the source and destination both have cards then check the source card's rank is higher and suit is same to ensure movement
        if source_card.check_rank_lower(destination_card) and destination_card.get_suit()==source_card.get_suit():
            return True
        
        return False
    
    # Function to check the validity of the foundation to tableau movement
    def valid_foundation_to_tableau_move(self,source_index,destination_index):
        # If source is empty
        if self.foundation[source_index].is_empty():
            return False

        # Peek the cards of source and destination
        destination_card = self.tableau[destination_index].peek()
        source_card = self.foundation[source_index].peek()

        # If the destination tableau is empty and the card being placed is King it is a valid move
        if (self.tableau[destination_index].is_empty() and source_card.get_rank()=="King"):
            return True

        # If the destination tableau is empty and source card is not an King it is not a valid move
        if (self.tableau[destination_index].is_empty() and source_card.get_rank()!="King"):
            return False
        
        # If the source and destination both have cards then check the card's rank and color to ensure the movement
        if destination_card.check_rank_lower(source_card) and destination_card.check_card_color()!=source_card.check_card_color():
            return True

        return False 
   
    # Function to check the validity of the foundation to tableau movement
    def valid_waste_to_tableau_move(self,destination_index):
        # If source is empty
        if self.stock_pile.get_waste_pile().is_empty():
            return False

        # Peek the cards of source and destination
        destination_card = self.tableau[destination_index].peek()
        source_card = self.stock_pile.peek()

        # If the destination tableau is empty and the source card being placed is King it is a valid move
        if (self.tableau[destination_index].is_empty() and source_card.get_rank()=="King"):
            return True

        # If the destination is empty and source card is not a king it is not a valid move
        if (self.tableau[destination_index].is_empty() and source_card.get_rank()!="King"):
            return False
        
        # If the source and destination both have cards then check the card's rank and color to ensure the movement
        if destination_card.check_rank_lower(source_card) and destination_card.check_card_color()!=source_card.check_card_color():
            return True
        
        return False

    # Function to check the validity of the foundation to tableau movement
    def valid_waste_to_foundation_move(self,destination_index):
        # If source is empty
        if self.stock_pile.get_waste_pile().is_empty():
            return False

        # Peek the cards of source and destination
        destination_card = self.foundation[destination_index].peek()
        source_card = self.stock_pile.peek()

        # If the destination foundation is empty and the card being placed is Ace it is a valid move
        if (self.foundation[destination_index].is_empty() and source_card.get_rank()=="Ace"):
            return True

        # If the destination is empty and source card is not an Ace it is not a valid move
        if (self.foundation[destination_index].is_empty() and source_card.get_rank()!="Ace"):
            return False
        
        # If the source and destination both have cards then check the source card's rank is higher and suit is same to ensure movement
        if source_card.check_rank_lower(destination_card) and destination_card.get_suit()==source_card.get_suit():
            return True
        
        return False
    
    # Moving multiple cards
    def move_multiple_cards(self,source_index,destination_index,card_name):
        try:
            
            # Function to capitalize the card name alphabets for better comparison
            card_name = game_files.utility.capitalize_card_name(card_name)
            
            # If card name is given empty
            if card_name == None:
                return "Enter a valid card name!"
            
            # Checks if the move is valid or not for multiple cards movement
            if not game_files.utility.valid_move(source_index,destination_index):
                return "Invalid move!"
            
            source_index = int(source_index)-1
            destination_index = int(destination_index)-1
            # If source is empty
            if self.tableau[source_index].is_empty():
                return "Invalid move!"

            # A card instance to compare it with the existing cards
            card = Card(0,0,card_name)

            # If source is empty
            if self.tableau[source_index].is_empty():
                return "Source is empty!"

            # Peek the cards of source and destination
            destination_card = self.tableau[destination_index].peek()
            source_card = self.tableau[source_index].find_card(card)

            # If no card is found
            if source_card==None:
                return "No such card found!"
            
            # If the card is found but face down
            if source_card.get_face_down():
                return "No such card found!"

            # If the destination tableau is empty and the source card being placed is King it is a valid move
            if (self.tableau[destination_index].is_empty() and source_card.get_rank()=="King"):
                self.count+=1
                self.move_cards(source_index,destination_index,card_name)
                return f"Card moved {str(source_card)} ---> {str(destination_card)}"

            # If the destination is empty and source card is not a king it is not a valid move
            if (self.tableau[destination_index].is_empty() and source_card.get_rank()!="King"):
                return "Invalid move!"
            
            # If the source and destination both have cards then check the card's rank and color to ensure the movement
            if destination_card.check_rank_lower(source_card) and destination_card.check_card_color()!=source_card.check_card_color():
                self.count+=1
                self.move_cards(source_index,destination_index,card_name)
                return f"Card moved {str(source_card)} ---> {str(destination_card)}"
            
            # If none of the condition is valid it means the card movement is not valid
            return "Invalid move!"
        
        except Exception as e:
            return f"An error occured: {e}"

    # Moving multiple cards from source to destination
    def move_cards(self,source_index,destination_index,card_name):
        # Using a temporary stack to store the cards of the source tableau
        cards = Stack()
        while(True):
            card = self.tableau[source_index].pop()
            # Loop continues till the card is found in the source tableau
            if card.get_card_name() == card_name:
                cards.push(card)
                break
            cards.push(card)

        # Pushing the cards into the destination tableau
        while not cards.is_empty():
            self.tableau[destination_index].push(cards.pop())
    
    # Drawing card from stock to waste pile
    def draw_card_from_stockpile(self):
        self.stock_pile.draw_card()
        self.count+=1
        
    # Win condition if all four foundations are filled by cards
    def game_win_condition(self):
        if self.stock_pile.is_empty():
            for i in range(7):
                if (not self.tableau[i].is_empty()):
                    current = self.tableau[i].get_elements()
                    while (current):
                        if(current.card.get_face_down()):
                            return "F"
                        current = current.next
            if(self.auto_move_cards()):
                return "C"

        for foundation in self.foundation:
            if foundation.cards_count()!=13:
                return "F"
        return "W"
    
    # Hint if any valid move available
    def get_hint(self):

        # Checking if valid move for tableau to foundation
        for i in range(7): # Iterating over the tableaus
            for j in range(4): # Iterating over the foundations
                # Checking move validity
                if self.valid_tableau_to_foundation_move(i, j):
                    self.hint_count+=1
                    return f"Hint: Move card {str(self.tableau[i].peek())} from Tableau {i+1} to Foundation {j+1}."
                
        # Checking if valid move for tableau to another tableau
        for i in range(7):  # Iterating over the tableaus
            for j in range(7):  # Iterating over the tableaus
                # Checking move validity
                if i != j and self.valid_tableau_to_tableau_move(i, j):
                    self.hint_count+=1
                    return f"Hint: Move card {str(self.tableau[i].peek())} from Tableau {i+1} to Tableau {j+1}."
        
        # Checking if valid move for waste to tableau
        for i in range(7): # Iterating over the tableaus
            # Checking move validity
            if self.valid_waste_to_tableau_move(i):
                self.hint_count+=1
                return f"Hint: Move card {str(self.stock_pile.peek())} from Waste to Tableau {i+1}."

        # Checking if valid move for waste to foundation
        for i in range(4): # Iterating over the foundations
            # Checking move validity
            if self.valid_waste_to_foundation_move(i):
                self.hint_count+=1
                return f"Hint: Move card {str(self.stock_pile.peek())} from Waste to Foundation {i+1}."

        return "No hint available!"

    # Automatically moving cards in the end
    def auto_move_cards(self):
        moved = True
        is_card_moved = False
        while(moved):
            moved=False
            for i in range(7):
                if not self.tableau[i].is_empty():
                    # Checking if valid move for tableau to foundation
                    for j in range(4): # Iterating over the foundations
                        # Checking move validity
                        if self.valid_tableau_to_foundation_move(i, j):
                            self.foundation[j].push(self.tableau[i].pop())
                            moved = True
                            is_card_moved=True
                    if moved:
                        moved = False
                        break
        return is_card_moved

    # Displaying current game state
    def display(self):
        try:
            # Displaying tableau
            print("\nTableau:\n")
            for i in range(7):
                print("Tableau "+str(i+1)+":",end=" ")
                self.display_list(self.tableau[i].get_elements())
                
            # Displaying Foundation
            print("\nFoundations:\n")
            for i in range(4):
                print("Foundation "+str(i+1)+":",end=" ")
                self.display_list(self.foundation[i].get_elements())
            
            print("\nStock Pile:", end=" ")
            if self.stock_pile.get_stock_pile().is_empty(): print(" No cards available!")
            else: print("Cards available")
            
            # Displaying waste pile
            print("\nWaste Pile:",end=" ")
            if self.stock_pile.get_waste_pile().is_empty():print("No cards available!")
            else: self.display_list(self.stock_pile.get_waste_pile().get_elements())
                    
            # Printing the moves and hints count
            print(f"\nMoves Count: {self.count}\nHints Count: {self.hint_count}")
        except Exception as e:
            print(f"An error occured: {e}")
    
    # Displaying cards for a single list head passed
    def display_list(self,head):
        if head==None:
            print()
            return

        cards = []
        current = head

        # Appending the cards into the array
        while current:
            cards.append(current.card)
            current = current.next
        
        # Popping and then printing each element so that the cards are printed in correct order
        while cards:
            card = cards.pop()
            # If card is found
            if card is not None:
                # If card is face down prints face down for the card
                if card.get_face_down():
                    print("Face-Down", end=" -> ")
                # If card is face up it prints card's rank and suit
                else:
                    print(str(card),end=" -> ")
                    
            # If card not found it breaks the loop
            else:
                break
        
        print()
        
    # Assisstance for the gui returning the cards
    def get_all_cards_for_list(self,head):
        # If the linked list is empty, return an empty list
        if head is None:
            return []

        # Temporary array to hold cards
        cards = []
        current = head

        # Iterate through the linked list and collect the cards
        while current:
            cards.append(current.card)
            current = current.next 

        cards.reverse()
        return cards

    # Loading from tableaus for gui
    def get_tableau_cards(self):
        tableau_images = []
        for tableau in self.tableau:
            # Get all the cards in the tableau
            tableau_images.append(self.get_all_cards_for_list(tableau.get_elements()))
        return tableau_images

    # Loading from foundations for gui
    def get_foundation_images(self):
        foundation_images = []
        for foundation in self.foundation:
            # Get all the cards in the foundation
            foundation_images.append(self.get_all_cards_for_list(foundation.get_elements()))
        return foundation_images

    # Loading from waste for gui
    def get_waste_pile_images(self):
        return self.get_all_cards_for_list(self.stock_pile.get_waste_pile().get_elements())