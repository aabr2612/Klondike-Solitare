# Card Class
class Card:
    # Constructor
    def __init__(self,rank,suit):
        self.__rank = rank # Rank of card
        self.__suit = suit # Suit of card
        self.__name = self.__set_card_name() # Giving card a short name to compare for easy movements
        self.__face_down = True # Face position of card
        self.__image_path = self.set_image_path() # Set a path of the image at start
    
    # Getters for the attributes
    def get_suit(self):
        return self.__suit
    
    def get_face_down(self):
        return self.__face_down
    
    def get_rank(self):
        return self.__rank
    
    def get_card_name(self):
        return self.__name
    
    # Setting the image path for the card
    def set_image_path(self):
        self.__image_path = f"assets/{self.__rank}_of_{self.__suit}.png"
    
    # Function to assign card a name
    def __set_card_name(self):
        ranks = {"Ace":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":11,"Queen":12,"King":13}
        return str(ranks[self.__rank])+self.__suit[0]
    
    # Returns the image path for the card
    def get_image_path(self):
        directory = "assets/"
        if self.__face_down:
            return directory+"face_down.png"
        else:
            return directory+self.__image_path

    # Redefining str function for card display
    def __str__(self):
        return f"{self.__rank} of {self.__suit} [{self.__name}]"
    
    # Flip card position
    def flip_card(self):
        self.__face_down = not self.__face_down
    
    # Check if card is lower than this one
    def check_rank_lower(self,source_card):
        ranks = {"Ace":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":11,"Queen":12,"King":13}
        return ranks[self.__rank] == ranks[source_card.get_rank()]+1
    
    # Checking the color of the card
    def check_card_color(self):
        return "Red" if self.__suit in ["Diamonds", "Hearts"] else "Black"