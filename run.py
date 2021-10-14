import math
import random
from colored import fg, bg, attr


class Player:
    players_battle_name = ""
    players_weapon = ""
    emenys_battle_name = ""
    enemys_weapon = ""
    player_score = 0
    enemy_score = 0
    final_score = 0


def get_player_battle_name():
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


def get_player_weapon_choice():
    print("Choose your weapon: Human, Cockroach or Nuclear Bomb")
    print("Type 'H' for Human, 'C' for Cockroach or 'NB' for Nuclear Bomb")

    while True:
        players_weapon = input("My weapon will be:\n")
        player.players_weapon = players_weapon

        if validate_players_weapon(players_weapon):
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


def get_enemy_battle_name():
    """
    Get random battle name for the computer
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


def get_enemy_weapon():
    """
    Get random weapons choice for the computer
    """
    weapons_choice = ['H', 'C', 'NB']
    computers_weapon = random.choice(weapons_choice)
    player.enemys_weapon = computers_weapon


def print_battle_outcome(name, weapon):

    color_nb = fg('#FF0000')
    color_c = fg('#FFA600')
    color_h = fg ('#00CFFF')
    res = attr("reset")

    print(f"{name} has selected:")
    if weapon == "H":
        print(color_h + h + res)
    elif weapon == "C":
        print(color_c + c + res)
    else:
        print(color_nb + nb + res)


def calculate_battle_results():

    if player.players_weapon == player.enemys_weapon:
        return "Tie"
    elif player.players_weapon == 'C' and player.enemys_weapon == 'NB':
        return "Win"
    elif player.players_weapon == 'H' and player.enemys_weapon == 'C':
        return "Win"
    elif player.players_weapon == 'NB' and player.enemys_weapon == 'H':
        return "Win"
    else:
        return "Lose"


def score_board():

    if calculate_battle_results() == "Win":
        print("You win!")
        player.player_score += 1
    elif calculate_battle_results() == "Lose":
        print("You lose!")
        player.enemy_score += 1
    else:
        print("It's a tie!")

    print("Score Board")
    print(f"{player.players_battle_name} - {player.player_score}")
    print(f"{player.emenys_battle_name} - {player.enemy_score} ")


def play_again():
    print("Would you like to play another round?")

    while True:
        try:
            player_replay = input("Type 'Y' for yes, or 'N' for no.")
            if player_replay == "Y":
                restart_game()
                break
            elif player_replay == "N":
                end_game()
                return "N"
                break
            else:
                raise ValueError(
                "You must provide a valid character"
            ) 
        except ValueError as e:
            print(f"Error: {e}")
            continue


def end_game():
    print(f"Thank you for playing {player.players_battle_name}.")
    print(f"You have battled {player.emenys_battle_name} and won a total of {player.player_score} times!")


def restart_game():
    get_player_weapon_choice()
    get_enemy_weapon()
    print_battle_outcome(player.players_battle_name, player.players_weapon)
    print_battle_outcome(player.emenys_battle_name, player.enemys_weapon)
    calculate_battle_results()
    score_board()
    play_again()


color_main = fg('#FFEB00')
res = attr("reset")

print("#################################################################")
print("--------- " + color_main + "Welcome to Human, Cockroach and Nuclear Bomb!" + res + " ---------")
print("#################################################################")
c = """
       ,--.     .--.
           \. ./
      /\/\/  "  \/\/\.
        /####|####\.
     /\{#####|#####}/|
   _/  {#Cockroach#} |
       /\####|####/|
      /  {###|###} |
       \  {##|##}  /
"""
nb = """
       _.-^-....,,--.
   .-/    Nuclear    \.
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
   /  Human    |
"""
player = Player()

get_player_battle_name()
get_player_weapon_choice()
get_enemy_battle_name()
get_enemy_weapon()
print_battle_outcome(player.players_battle_name, player.players_weapon)
print_battle_outcome(player.emenys_battle_name, player.enemys_weapon)
calculate_battle_results()
score_board()
play_again()
