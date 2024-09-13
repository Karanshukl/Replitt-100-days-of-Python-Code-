import os
import time as t
from datetime import datetime

dairy = {}  # Use a dictionary to store entries with timestamp as the key

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add_dairy():
    entry = input("What do you want to add to the dairy? ")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current time in a readable format
    dairy[timestamp] = entry  # Store entry with timestamp as the key
    clear_screen()
    print(f"Entry added at {timestamp}\n")
    t.sleep(2)

def view_dairy():
    usernames = ["Karan", "Carlos", "Hradesh", "Boss"]
    passwords = ["12345678", "Karan7680"]

    username = input("Enter your Username: ").title()
    password = input("Enter your Password: ")  # Keep passwords case-sensitive

    if username in usernames and password in passwords:
        print("Login Successful ✅\n")
        if dairy:
            print("Your dairy entries:\n")
            for timestamp, entry in dairy.items():
                print(f"{entry} - [{timestamp}]")
        else:
            print("No entries in the dairy yet.")
    else:
        print("Wrong username or password!")

    t.sleep(5)
    clear_screen()

def main():
    running = True
    while running:
        try:
            main_menu = int(input("""\nWhat do you choose:
1. Add to Dairy
2. View Dairy
3. Exit\n> """))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if main_menu == 1:
            add_dairy()
        elif main_menu == 2:
            view_dairy()
        elif main_menu == 3:
            running = False
        else:
            print("Invalid choice, please try again.")

        clear_screen()

main()
