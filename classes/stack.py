from classes.linkedlist import LinkedList

# Stack Class
class Stack:
    # Constructor
    def __init__(self):
        self.__linkedList = LinkedList()
        self.__size = 0
    
    # Pushing the card into the stack
    def push(self,card):
        self.__size +=1
        self.__linkedList.insert_at_head(card)
    
    # Popping the card from stack
    def pop(self):
        # Checks size if greater than 0 it pops the card from the stack
        if self.__size -1>=0:
            self.__size -=1
            return self.__linkedList.remove_from_head()
        return None

    # Viewing the top card in the stack
    def peek(self):
        # If the size of the stack is greater than 0
        if self.is_empty():
            return None
        return self.__linkedList.view_first_node()
    
    # Finding a card in stack
    def find_card(self,card_name):
        if self.is_empty():
            return None

        return self.__linkedList.find_node(card_name)

    # Number of cards in stack
    def cards_count(self):
        return self.__size
    
    # Flipping all cards in the stack
    def flip_cards(self):
        if self.__size>0:
            self.__linkedList.flip_cards()

    # Display function to display cards
    def get_elements(self):
        return self.__linkedList.get_head()

    # Checks if the stack is empty
    def is_empty(self):
        return self.__linkedList.is_empty()