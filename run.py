import math
import random


class Player:
    battle_name = ""
    players_weapon = ""
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
        battle_name = input("Enter your battle name here:\n")
        player.battle_name = battle_name

        if validate_battle_name(battle_name):
            print(f"Welcome to the battle, {battle_name} \n")
            break

    print("Choose your weapon: Human, Cockroach or Nuclear Bomb")
    print("Type 'H' for Human, 'C' for Cockroach or 'NB' for Nuclear Bomb")
    
    while True:
        players_weapon = input("My weapon will be:\n")
        player.players_weapon = players_weapon

        if validate_players_weapon(players_weapon):
            print("You have choosen:") 
            if player.players_weapon == "H":
                print(h)
            elif player.players_weapon == "C":
                print(c)
            else:
                print(nb)
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
    weapons_choice = ['H', 'C', 'NB']
    computers_weapon = random.choice(weapons_choice)
    player.enemys_weapon = computers_weapon
    print(f"Your enemy has chosen:")
    if player.enemys_weapon == "H":
        print(h)
    elif player.enemys_weapon == "C":
        print(c)
    else:
        print(nb)

def calculate_battle_results():
    if player.players_weapon == player.enemys_weapon:
        print("It's a tie!")
    elif player.players_weapon == 'C' and player.enemys_weapon == 'NB':
        print("You win!")
    elif player.players_weapon == 'H' and player.enemys_weapon == 'C':
        print("You win!")
    elif player.players_weapon == 'NB' and player.enemys_weapon == 'H':
        print("You win!")
    else:
        print("You loose!")



print("Welcome to Human, Cockroach and Nuclear Bomb! \n")
c = """
      ,--.     .--. 
      /    \. ./    \ 
     /  /\/  "  \/\  \ 
    / _/ /~~~v~~~\ \_ \ 
        /####|####\     
     /\{#####|#####}/\   
   _/  {#####|#####}  \_  
  |   /{#####|#####}\   | 
  |  / {#####|#####} \  | 
  | /  {#####|#####}  \ | 
  |  \ \#####|#####/ /  | 
   \  \ \####|####/ /  / 
    \     \##|##/     /  
"""
nb = """
     _.-^^---....,,--       
 _--                  --_  
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
"""
h = """
      ////\\\\
      |      |
     @  O  O  @
      |  ~   |         \__
       \ -- /          |\ |
     ___|  |___        | \|
    /          \      /|__|
   /            \    / /
  /  /| .  . |\  \  / /
 /  / |      | \  \/ /
"""
player = Player()
get_player_data()
get_computers_weapon()
calculate_battle_results()