import random
from classes.card import Card

# Deck Class
class Deck:
    # Constructor
    def __init__(self):
        self.__cards = [] # Array to hold the cards
        self.__loadCards() # Function to load the cards
        self.__shuffle_cards_randomly() # Function to shuffle the cards when deck is once made

    # Loading the cards for the deck
    def __loadCards(self):
        suits = ["Diamonds", "Hearts", "Spades", "Clubs"] # Suits
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"] # Ranks
        
        # Loading card one by one for suits according to ranks
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.__cards.append(card)

    # Using random function to shuffle cards randomly
    def __shuffle_cards_randomly(self):
        random.shuffle(self.__cards)

    # Function to draw a card
    def draw_card(self):
        # If cards are present in the deck
        if self.__cards:
            return self.__cards.pop()
        
        return None

    # Function to display all cards of the deck
    def get_cards(self):
        return self.__cards