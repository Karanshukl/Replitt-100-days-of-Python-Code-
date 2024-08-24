import random  # Importing the random module to generate random numbers.
import os   # Importing the os module to clear screen
import time as t    # Importing the time module for timeout 

# Function to generate a random number between 1 and 90.
def generate_number():
    return random.randint(1, 90)

# Function to print the Bingo card in a formatted way.
def print_card(card):
    for row in card:  # Loop through each row in the Bingo card.
        print("\t|\t".join(map(str, row)))  # Join the items in the row with tabs and print them.
        print()  # Print a new line after each row for better readability.

# Function to create the Bingo card.
def create_bingo_card():
    # Generate 8 unique random numbers between 1 and 90 and sort them.
    numbers = sorted(random.sample(range(1, 91), 8))
    # Create a 3x3 Bingo card with a "BG" (Bingo) in the center.
    return [
        [numbers[0], numbers[1], numbers[2]],  # First row of the card.
        [numbers[3], "BG", numbers[4]],        # Second row with "BG" in the center.
        [numbers[5], numbers[6], numbers[7]],  # Third row of the card.
    ]

# Function to play the Bingo game.
def play_bingo():
    card = create_bingo_card()  # Create the Bingo card.
    while True:  # Infinite loop to keep the game running.
        print_card(card)  # Print the Bingo card.
        number = int(input("Next Number: "))  # Ask the player for the next number.
        for row in range(3):  # Loop through each row in the card.
            for col in range(3):  # Loop through each item in the row.
                if card[row][col] == number:  # Check if the number is on the card.
                    card[row][col] = "X"  # Mark the number with an "X" if found.
        # Check if the player has won by counting the number of "X"s on the card.
        if sum(row.count("X") for row in card) == 8:
            print("\033[34mYou have won!")  # Print a win message if all 8 numbers are marked.
            break  # Exit the loop, ending the game.
        
        os.system("clear")
        t.sleep(1)

play_bingo()
