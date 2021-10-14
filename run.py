import math
import random


class Player:
    players_battle_name = ""
    players_weapon = ""
    emenys_battle_name = ""
    enemys_weapon = ""
    final_score = 0


def get_player_data():
    """
    Get player details: battle name and weapon choice
    """

    print("Please enter your battle name")
    print("Battle names can have a maximum of 20 characters,")
    print("and spaces must be replaced by an underscore")
    print("(for example: ana_banana) \n")

    while True:
        players_battle_name = input("Enter your battle name here:\n")
        player.players_battle_name = players_battle_name

        if validate_battle_name(players_battle_name):
            print(f"Welcome to the battle, {players_battle_name} \n")
            break

    print("Choose your weapon: Human, Cockroach or Nuclear Bomb")
    print("Type 'H' for Human, 'C' for Cockroach or 'NB' for Nuclear Bomb")

    while True:
        players_weapon = input("My weapon will be:\n")
        player.players_weapon = players_weapon

        if validate_players_weapon(players_weapon):
            break


def validate_battle_name(players_battle_name):
    """
    Raise an Error in case battle name has more than 20 characters,
    and/or has a space character.
    """
    try:
        if len(players_battle_name) > 20:
            raise ValueError(
                "Battle names can have a maximum of 20 characters."
            )
        elif ' ' in players_battle_name:
            raise ValueError(
                "You must use underscore to represent spaces"
            )
    except ValueError as e:
        print(f"Error: {e}. Please try again")
        return False

    return True


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
    enemy_names_choice = [
        "Doctor Who",
        "Robocop",
        "Paranoid Android",
        "Hardly Human",
        "C3PO"
    ]
    enemys_name = random.choice(enemy_names_choice)
    player.emenys_battle_name = enemys_name

    weapons_choice = ['H', 'C', 'NB']
    computers_weapon = random.choice(weapons_choice)
    player.enemys_weapon = computers_weapon


def print_battle_outcome(name, weapon):

    print(f"{name} has selected:")
    if weapon == "H":
        print(h)
    elif weapon == "C":
        print(c)
    else:
        print(nb)


def calculate_battle_results():
    if player.players_weapon == player.enemys_weapon:
        print("It's a tie!")
        return "Tie"
    elif player.players_weapon == 'C' and player.enemys_weapon == 'NB':
        print("You win!")
        return "Win"
    elif player.players_weapon == 'H' and player.enemys_weapon == 'C':
        print("You win!")
        return "Win"
    elif player.players_weapon == 'NB' and player.enemys_weapon == 'H':
        print("You win!")
        return "Win"
    else:
        print("You loose!")
        return "Loose"


def score_board():
    players_score = 0
    enemys_score = 0

    if calculate_battle_results() == "Win":
        players_score += 1
    elif calculate_battle_results() == "Loose":
        enemys_score += 1
    else:
        pass

    print("Score Board")
    print(f"{player.players_battle_name} - {players_score}")
    print(f"{player.emenys_battle_name} - {enemys_score} ")


print("Welcome to Human, Cockroach and Nuclear Bomb! \n")
c = """
       ,--.     .--.
           \. ./
        /\/  "  \/|
        /####|####\   
     /\{#####|#####}/|
   _/  {#Cockroach#} |
       /\####|####/|
       / {###|###} |
       \  {##|##}  /
"""
nb = """
       _.-^-....,,--      
   .-/    Nuclear    \_  
   ._      Bomb      /  
    ```--. . , ; .--''      
          |     |             
       .-=|     |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
"""
h = """
      ////////
      |      |
     {  o  o  }
      |  ^   |
       \ -- /
     ___|  |___
   /  Human    \ 
"""
player = Player()
get_player_data()
get_computers_weapon()
print_battle_outcome(player.players_battle_name, player.players_weapon) 
print_battle_outcome(player.emenys_battle_name, player.enemys_weapon)
calculate_battle_results()
score_board()
