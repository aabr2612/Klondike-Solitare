from classes.linkedlist import LinkedList

# Stack Class
class Stack:
    # Constructor
    def __init__(self):
        self.__linkedList = LinkedList()
        self.__size = 0
    
    # Pushing the element into the stack
    def push(self,element):
        self.__size +=1
        self.__linkedList.insert_at_head(element)
    
    # Popping the element from stack
    def pop(self):
        # Checks size if greater than 0 it pops the element from the stack
        if not self.is_empty():
            self.__size -=1
            return self.__linkedList.remove_from_head()
        return None

    # Viewing the top element in the stack
    def peek(self):
        # If stack is empty
        if self.is_empty():
            return None
        # Else
        return self.__linkedList.view_first_node()
    
    # Finding an element in stack
    def find_card(self,card):
        if self.is_empty():
            return None

        return self.__linkedList.find_node(card)

    # Number of cards in stack
    def cards_count(self):
        return self.__size

    # Returns the top element in stack
    def get_top(self):
        return self.__linkedList.get_head()

    # Checks if the stack is empty
    def is_empty(self):
        return self.__linkedList.is_empty()