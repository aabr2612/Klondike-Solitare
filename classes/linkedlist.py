# Node Class
class Node:
    # Constructor
    def __init__(self, card):
        self.card = card  # Card
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

        # If head is not empty, removing card from it
        temp = self.__head
        self.__head = self.__head.next

        # Flipping the head card if needed
        if self.__head.card.get_face_down():
            self.__head.card.flip_card()
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

        # Return the head node's card
        return self.__head.card

    # Finding a specific node by card name in list
    def find_node(self, card_name):
        # If list is empty
        if self.is_empty():
            return None

        # If list is not empty
        current = self.__head
        # Loop continues until a specific card is found, else returns None
        while current:
            if current.card.get_card_name() == card_name:  # If card name matches
                return current.card
            current = current.next
        return None  # Return None if card is not found

    # Flipping all cards in the linked list
    def flip_cards(self):
        # If the linked list is empty, do nothing
        if self.is_empty():
            return

        # Flip the cards so that all cards are face up
        current = self.__head
        while current:
            # Flip the card if it is face down
            if not current.card.get_face_down():
                current.card.flip_card()
            current = current.next

        # Ensuring that the head card is always visible
        self.__head.card.flip_card()