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
    print(f"Welcome to the battle, {battle_name}")


print("Welcome to Human, Cockroach and Nuclear Bomb! \n")
get_player_data()
