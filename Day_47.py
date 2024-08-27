import random

cards = [
    {"name": "Ram", "Power": 45, "Intelligence": 8, "Courage": 31, "Speed": 35, "Anger": 3},
    {"name": "Harry ", "Power": 70, "Intelligence": 9, "Courage": 85, "Speed": 60, "Anger": 6},
    {"name": "Hulk", "Power": 65, "Intelligence": 10, "Courage": 75, "Speed": 90, "Anger": 4},
    {"name": "Shiv", "Power": 50, "Intelligence": 7, "Courage": 70, "Speed": 40, "Anger": 5},
    {"name": "Dhoni", "Power": 55, "Intelligence": 8, "Courage": 25, "Speed": 30, "Anger": 2},
    {"name": "Lakshman", "Power": 60, "Intelligence": 6, "Courage": 45, "Speed": 75, "Anger": 30},
    {"name": "Marcus", "Power": 40, "Intelligence": 5, "Courage": 60, "Speed": 50, "Anger": 4},
    {"name": "Rock", "Power": 80, "Intelligence": 10, "Courage": 50, "Speed": 90, "Anger": 2},
    {"name": "God", "Power": 55, "Intelligence": 7, "Courage": 75, "Speed": 65, "Anger": 6},
    {"name": "Indra", "Power": 70, "Intelligence": 9, "Courage": 80, "Speed": 50, "Anger": 7},
    {"name": "Ganesh", "Power": 95, "Intelligence": 10, "Courage": 95, "Speed": 100, "Anger": 5},
    {"name": "Hanuman ", "Power": 100, "Intelligence": 10, "Courage": 100, "Speed": 100, "Anger": 10}
]
print()

def printList():
    print("CHOSE YOUR CHAMPION")
    print()
    for i, character in enumerate(cards, start=1):
        print(f"{i}. {character['name']}")

def pickCharacter():
    while True:
        choice = input("Chose your Hero: ")
        if choice.isdigit():
            choice = int(choice)
            if -1 <= choice < len(cards)+1:
                break
            else:
                print("Enter a valid number")
        else:
            print("Enter a valid number")
    return choice

def extraSetup(choice):
    print("")
    player_character = cards[choice - 1]
    computer_candidates = [character for character in cards if character != player_character]
    computer_character = random.choice(computer_candidates)
    player_character_name = player_character["name"]
    computer_character_name = computer_character["name"]
    print(f"You picked: {player_character_name}")
    print(f"AI picked: {computer_character_name}")

    return player_character, computer_character

def pickCategory():
    print("")
    stat = input("Pick the stat: Power, Intelligence, Courage, Speed, Anger\n: ")
    return stat

def playGame(player_character, computer_character, stat):
    player_stat = player_character[stat]
    computer_stat = computer_character[stat]
    print()                                               
    print(f"Player {stat}: {player_stat}")
    print(f"AI {stat}: {computer_stat}")
    print()
    if player_stat > computer_stat:
        print(f"You win! {player_character['name']} has {stat} of {player_stat}")
    elif player_stat < computer_stat:
        print(f"AI wins! Ai has {stat} of {computer_stat}")
    else:
        print(f"It's a tie! ")
        print()

printList()
choice = pickCharacter()
player_character, computer_character = extraSetup(choice)
stat = pickCategory()
playGame(player_character, computer_character, stat)
