import math
import random


class Player:
    battle_name = ""
    final_score = 0

def get_player_data():
    """
    Get player details
    """

    print("Please enter your battle name")
    print("Battle names can have a maximum of 20 characters,")
    print("and spaces must be replaced by an underscore")
    print("(for example: ana_banana) \n")

    while True:
        battle_name = input("Enter your battle name here:")
        player.battle_name = battle_name

        if validate_battle_name(battle_name):
            print(f"Welcome to the battle, {battle_name} \n")
            break

def validate_battle_name(battle_name):
    """
    Raise an Error in case battle name has more than 20 characters, 
    and/or has a space character. 
    """
    try:
        if len(battle_name) > 20:
            raise ValueError(
                f"Battle names can have a maximum of 20 characters. Yours has {len(battle_name)}"
            )
        elif ' ' in battle_name:
            raise ValueError(
                f"You must use underscore to represent spaces"
            )
    except ValueError as e:
        print(f"Error: {e}. Please try again")
        return False
    
    return True

def get_players_weapon():
    """
    Get player's weapon of choice
    """

    print("Choose your weapon: Human, Cockroach or Nuclear Bomb")
    print("Type 'H' for Human, 'C' for Cockroach or 'NB' for Nuclear Bomb")
    
    while True:
        players_weapon = input("My weapon will be:")

        if validate_players_weapon(players_weapon):
            print(f"You have choosen {players_weapon} \n")
            break

def validate_players_weapon(players_weapon):
    """
    Raise an Error in case user input does not match available weapons. 
    """
    try:
        if players_weapon != "H" and players_weapon != "C" and players_weapon != "NB":
            raise ValueError(
                f"{players_weapon} is not a valid weapon"
            )
    except ValueError as e:
        print(f"Error: {e}. Please try again")
        return False
    
    return True

def get_computers_weapon():
    """
    Get random weapons choice for the computer
    """
    weapons_choice = ['paper', 'scissors', 'rock']
    computers_weapon = random.choice(weapons_choice)
    print(computers_weapon)

print("Welcome to Human, Cockroach and Nuclear Bomb! \n")
player = Player()
get_player_data()
get_players_weapon()
get_computers_weapon()