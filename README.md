# Klondike Solitaire - Python Implementation

## Overview

Klondike Solitaire is a classic single-player card game where the goal is to move all 52 cards into four foundation piles. This game implemnted in Python focuses on the use of **Data Structures (DSA)** to manage the game logic effectively. Custom-built data structures like stacks, queues, and linked lists are used to to handle card movements and ensure valid gameplay.

This project shows the effective application of **Data Structures** and **Object-Oriented Programming** (OOP) principles.

## Key Features

### 1. **Single Card Movements**
- Move a single card between the tableau, foundation, and waste pile, according to the game's rules.

### 2. **Multiple Card Movements**
- Move multiple cards between tableau piles, as long as the sequence follows the rules (alternating colors and descending ranks).

### 3. **Draw Cards from the Stockpile**
- Draw cards from the stockpile to the waste pile, with the top card of the waste pile available for valid moves.

### 4. **Move Validations**
- All card movements are validated to ensure that they adhere to the game's rules based on rank and suit.

### 5. **Move Hint**
- Suggests valid moves when the player is stuck, making use of the current game state to identify possible moves.

### 6. **Auto-Win**
- Automatically moves valid cards to the foundation piles as the win condition meets.

### 7. **Win Game**
- The game ends when all cards are successfully moved to the foundation piles, followed by a congratulations message, number of hints used and the moves made.

### 8. **Backend flexibility**
- The backend is flexible enough to work with any UI interface (GUI or Console based).

## DSA in Klondike Solitaire

### 1. **Stacks (Linked List-based)**

Stacks are used for the tableau, foundation, and waste piles, which adhere to the **Last-In-First-Out (LIFO)** principle:
- **Tableau Piles**: Cards are moved based on descending order and alternating colors.
- **Foundation Piles**: Cards are added in ascending order (Ace to King).
- **Waste Pile**: Cards are managed in sequence, drawn or removed.

Stacks are implemented with linked lists, ensuring operations like(`push`, `pop`, `peek`).

### 2. **Queues (Implemented with Two Stacks)**

The **stockpile** and **waste pile** are managed using a **queue**, implemented with two stacks, following the **First-In-First-Out (FIFO)** principle:
- **Stockpile**: Cards that haven't been drawn are managed in FIFO order.
- **Waste Pile**: Cards drawn from the stockpile are added to the waste pile, with the queue structure rebringing them back when the stockpile is empty.

### 3. **Linked Lists**

Linked lists allow dynamic storage for cards, enabling efficient insertions and deletions without pre-defined sizes. This structure supports:
- **Card movement**: Efficiently manages the card movement.
- **Card Representation**: Each card is a node, simplifying management.

### 4. **Arrays**

Arrays are used for storing the deck cards and while moving and displaying cards in correct order.

## OOP Usage

**Object-Oriented Programming**:

  - **Encapsulation**: Card attributes and game logic are encapsulated in well-defined classes.
  - **Composition**: The `Game` class utilizes `Stack` and `Queue` objects for managing piles.
  - **Abstraction**: High-level methods abstract complex card movements and game rules.
  - **Method overriding**: Methods like `__str__()` and `__init__()` provide a string representation and initialize game components.

## Backend Architecture

The backend consists of the following files:

- **Card.py:** 
   Card class implementation with attributes suit, rank, face_down, and name.

- **Deck.py:** Deck class array of 52 cards. It loads, shuffles, and then allows drawing cards using the method `draw_card`, which is used in the game to distribute cards among the tableau and foundation piles.

- **LinkedList.py:** Linked list data structure is implemented to create stacks used for tableaus and foundations. It facilitates moving multiple cards between the tableaus and other piles.

- **Queue.py:** Queue data structure is implemented using two stacks to handle the stockpile and waste pile functionality. It allows drawing cards from the stockpile to the waste pile and drawing the top card from the waste pile.

- **Stack.py:** Stack data structure is implemented using a linked list, helping to implement the tableaus and foundation piles, along with the queue class used for the stockpile.

- **Game.py:** The Game class initializes the tableaus, foundations, stockpile, and deck. It then uses the deck to distribute the cards among the tableaus and stockpile. It contains the logic for card movements, multiple card movements, and the hint system.

- **Utility.py:** The utility file contains validation functions that ensure correct indexes and piles, verifying that cards are moved to the correct destination from the source.

## Frontend Architecture

The frontend is currently implemented in console. It has following files:

- **UI.py:** UI contains the header and other menus implementation alongwith win game menu which is implemented in CLI which allows the user to interact with the backend to perform tasksusing the ui.

- **Main.py:** Main file contains all the driver code which interacts withthe UI and Game files to make a flow of the game.


## Game Flow

The game flow proceeds as follows:

1. **Main Menu**:
   Upon running the `main.py` file, the main menu appears with the following options:

   - **Play Game**: 
     If the user selects to play the game, the game screen is displayed with a sub-menu of game options:
     
     - **1. Draw Card**: 
       Allows the user to draw a card from the stockpile.
     
     - **2. Move Card**: 
       Allows the user to move a single card between the game piles.
     
     - **3. Move Multiple Cards**: 
       Allows the user to move multiple cards from one pile to another within the game.
     
     - **4. Get Hint**: 
       Provides a hint for a valid move, helping the user when they are stuck.
     
     - **5. Exit**: 
       Ends the current game session.

   - **Instructions**: 
     Displays the instructions for playing the game.

   - **Exit**: 
     Closes the game and exits the application.


## Folder Structure

The project follows a well-organized folder structure for ease of development and maintenance:

    Here is the folder structure for the game:

        Solitaire
        ├── Classes
        │   ├── card.py
        │   ├── deck.py
        │   ├── linkedlist.py
        │   ├── queue.py
        │   └── stack.py
        ├── Game Files
        │   ├── game.py
        │   └── utility.py
        ├── UI
        │   └── ui.py
        └── main.py

## How to Run the Game

   To run the game, follow these steps:

1. **Clone the repository**:
   ```bash
        git clone https://github.com/aabr2612/solitaire
2. **Navigate folder**

        cd solitaire

3. **Run the main.py file:**

        main.py

## Conclusion
   This Klondike Solitaire project focuses on the effective use of **Data Structures (DSA)**, such as **stacks**, **queues**, and **linked lists**, to efficiently manage card movements and game rules. 