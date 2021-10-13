import math
import random

def get_player_data():
    """
    Get player details
    """
    print("Please enter your battle name")
    print("Battle names can have a maximu of 20 characters,")
    print("and spaces must be separated by an underscore")
    print("(for example: ana_banana) \n")

    battle_name = input("Enter your battle name here:")
    validate_battle_name(battle_name)

    #print(f"Welcome to the battle, {battle_name}")

def validate_battle_name(battle_name):
    """
    Raise an Error in case battle name has more than 20 characters, 
    and/or has a space character. 
    """
    try:
        if len(battle_name) > 20:
            raise ValueError(
                f"Battle names can mave a maximum of 20 characters. Yours has {len(battle_name)}"
            )
        elif ' ' in battle_name:
            raise ValueError(
                f"You must use underscore to represent spaces"
            )
    except ValueError as e:
        print(f"Error: {e}. Please try again")


print("Welcome to Human, Cockroach and Nuclear Bomb! \n")
get_player_data()
