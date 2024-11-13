# Node Class
class Node:
    # Constructor
    def __init__(self, card):
        self.card = card  # Card or any data (Saying card as mostly used for cards)
        self.next = None  # Next

# LinkedList Class
class LinkedList:
    # Constructor
    def __init__(self):
        self.__head = None

    # Function to insert element at the head
    def insert_at_head(self, card):
        new_node = Node(card)

        # If the head is none then set the new node as head
        if self.is_empty():
            self.__head = new_node

        # If head already present then set the new node as head and set its next to previous head
        else:
            new_node.next = self.__head
            self.__head = new_node

    # Function to remove element from the head
    def remove_from_head(self):
        # If linkedlist is empty
        if self.is_empty():
            print("No more cards!")
            return None

        # If head is the only element in the linkedlist set the head to None to indicate that the linkedlist is empty
        if self.__head.next is None:
            temp = self.__head
            self.__head = None
            return temp.card

        # If head is not empty, removing element from it
        temp = self.__head
        self.__head = self.__head.next

        return temp.card

    # Function to get the head of the linked list
    def get_head(self):
        return self.__head

    # Function to check if the linked list is empty
    def is_empty(self):
        return self.__head is None

    # Check the first node (head) of the list
    def view_first_node(self):
        # If list is empty
        if self.is_empty():
            return None

        # Return the head node's value
        return self.__head.card

    # Finding a specific node by element in list
    def find_node(self, card):
        # If list is empty
        if self.is_empty():
            return None

        # If list is not empty
        current = self.__head

        # Loop continues until a specific element is found, else returns None
        while current:
            if current.card==card:  # If element matches
                return current.card
            current = current.next
        return None  # Return None if element not found
