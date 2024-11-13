from classes.stack import Stack

# Queue Class
class Queue:
    # Constructor
    def __init__(self):
        self.__stock_pile = Stack()
        self.__waste_pile = Stack()
        self.__size = 0

    # Enqueue card into the queue
    def enqueue(self,card):
        self.__size += 1
        self.__stock_pile.push(card)
    
    # Removing card from the queue
    def dequeue(self):
        # If waste pile is empty
        if self.__waste_pile.is_empty():
            return None

        # If waste pile is empty
        card = self.__waste_pile.pop()
        self.__size -= 1

        # If after removing card waste pile is not empty flipping the existing cards for showing the cards
        if not self.__waste_pile.is_empty():
            self.__waste_pile.flip_cards()
        return card
    
    # Peek for queue
    def peek(self):
        return self.__waste_pile.peek()
    
    # Drawing card from stock to waste pile
    def draw_card(self):
        # If stock and waste 
        if self.__stock_pile.is_empty() and self.__waste_pile.is_empty():
            return
        
        if self.__stock_pile.is_empty():
            while not self.__waste_pile.is_empty():
                self.__stock_pile.push(self.__waste_pile.pop())
            return
        
        card = self.__stock_pile.pop()
        self.__waste_pile.push(card)
        self.__waste_pile.flip_cards()
    
    # Number of cards in queue
    def cards_count(self):
        return self.__size

    # Checks if the queue is empty
    def is_empty(self):
        return self.__size == 0
    
    # Getters for the attributes
    def get_stock_pile(self):
        return self.__stock_pile

    def get_waste_pile(self):
        return self.__waste_pile
    