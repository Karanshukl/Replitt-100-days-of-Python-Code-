
import replit
from replit import db 
import datetime
import os
import time


def add_tweet():
    """
    Prompts the user for a tweet, adds it to the Replit database with a timestamp,
    and clears the screen.
    """

    tweet = input(" > ")
    timestamp = datetime.datetime.now().isoformat()  # Use ISO 8601 format for timestamps
    key = f"mes{timestamp}"
    db[key] = tweet
    time.sleep(1)
    os.system("clear")  # Clear the screen after adding tweet


def view_tweets():
    """
    Retrieves all tweets from the Replit database in reverse chronological order,
    paginates them (10 per page), and displays them to the user.
    """

    matches = db.prefix("mes")
    matches = matches[::-1]  # Reverse order (latest first)

    counter = 0
    for i in matches:
        print(db[i])
        print()
        time.sleep(0.3)  # Add a slight pause between tweets
        counter += 1

        if counter % 10 == 0:
            carry_on = input("Next 10?: ").lower()  # Ensure case-insensitive input
            if carry_on == "no":
                break

    time.sleep(1)
    os.system("clear")  # Clear the screen after viewing tweets


def main():
    """
    The main loop of the program, presenting the menu and handling user input.
    """

    while True:
        print("Tweeter\n")
        menu = input("1: Add Tweet\n2: View Tweets\n > ")
        if menu == "1":
            add_tweet()
        elif menu == "2":
            view_tweets()
        else:
            print("Invalid input. Please enter 1 or 2.")


if __name__ == "__main__":
    main()  # Run the main loop
