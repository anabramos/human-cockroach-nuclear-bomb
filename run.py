import random
import os
from colored import fg, attr


class Player:
    players_battle_name = ""
    players_weapon = ""
    enemys_battle_name = ""
    enemys_weapon = ""
    player_score = 0
    enemy_score = 0


def game_intro():
    """
    Print game title, instructions and rules at the begiining of every game.
    """
    print(hash_line)
    print("--------- " + color_blue + "Welcome to Human, Cockroach and Nuclear Bomb!" + res + " ---------")
    print(hash_line)
    print(text_box_rules)


def get_player_battle_name():
    """
    Get player battle name.
    """
    print(hash_line)
    print("Please create your battle name")
    print("- Use a max. of 20 characters, and underscores to replace spaces")
    print("- For example: ana_banana")

    while True:
        players_battle_name = input(color_yellow + "Enter your battle name here:\n" + res)
        player.players_battle_name = players_battle_name
        os.system('cls' if os.name == 'nt' else 'clear')
        print(hash_line)

        if validate_battle_name(players_battle_name):
            print(color_blue + f"Welcome to the battle, {players_battle_name}" + res)
            print(hash_line)
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
    """
    Get player weapon choice.
    """

    print("Choose your weapon:")
    print(" - Type 'H' for Human, 'C' for Cockroach or 'NB' for Nuclear Bomb")

    while True:
        players_weapon = input(color_yellow + "My weapon will be:\n" + res)
        os.system('cls' if os.name == 'nt' else 'clear')
        player.players_weapon = players_weapon

        if validate_players_weapon(players_weapon):
            break


def validate_players_weapon(players_weapon):
    """
    Raise an Error in case user input for weapon choice is not available.
    """
    try:
        if players_weapon != "H" and players_weapon != "C" and players_weapon != "NB":
            raise ValueError(
                f"{players_weapon} is not a valid weapon"
            )
    except ValueError as e:
        print(f"Error: {e}. Please try again")
        print("Type 'H' for Human, 'C' for Cockroach or 'NB' for Nuclear Bomb")
        return False

    return True


def get_enemy_battle_name():
    """
    Get random battle name for the computer.
    """
    enemy_names_choice = [
        "Doctor Who",
        "Robocop",
        "Paranoid Android",
        "Hardly Human",
        "C3PO"
    ]
    enemys_name = random.choice(enemy_names_choice)
    player.enemys_battle_name = enemys_name


def get_enemy_weapon():
    """
    Get random weapons choice for the computer.
    """
    weapons_choice = ['H', 'C', 'NB']
    computers_weapon = random.choice(weapons_choice)
    player.enemys_weapon = computers_weapon


def print_battle_outcome(name, weapon):
    """
    Print weapon choice of player and enemy(computer).
    """

    print(f"{name} has selected:")
    if weapon == "H":
        print(color_lightblue + H + res)
    elif weapon == "C":
        print(color_orange + C + res)
    else:
        print(color_red + NB + res)


def calculate_battle_results():
    """
    Based on player and computer's weapon choice, define is player wins or loses.
    """

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
    """
    Print the score of each player at the end of each battle,
    add up score for every win (player) and lost (enemy),
    and add nothing when it is a tie.
    """

    if calculate_battle_results() == "Win":
        print(color_green + "You win!" + res)
        player.player_score += 1
    elif calculate_battle_results() == "Lose":
        print(color_red + "You lose!" + res)
        player.enemy_score += 1
    else:
        print(color_yellow + "It's a tie!" + res)

    print("Score:")

    print(f"{player.players_battle_name} {player.player_score} x {player.enemy_score} {player.enemys_battle_name}")
    print(hash_line)


def play_again():
    """
    Ask player if they would like to play another round.
    If yes, run restart game function.
    If not, run end game function.
    """
    print("Would you like to play another round?")

    while True:
        try:
            player_replay = input(color_yellow + "Type 'Y' for yes, or 'N' for no. \n" + res)
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
    """
    Stop running the game, and print game overview to the player,
    including name of enemy and number of wins.
    """

    print(color_lightblue + f"Thank you for playing {player.players_battle_name}.")
    print(f"You have battled {player.enemys_battle_name} and won a total of {player.player_score} times!" + res)


def restart_game():
    """
    Run extra game round including only relevant functions.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    get_player_weapon_choice()
    get_enemy_weapon()
    print_battle_outcome(player.players_battle_name, player.players_weapon)
    print_battle_outcome(player.enemys_battle_name, player.enemys_weapon)
    calculate_battle_results()
    score_board()
    play_again()


def main():
    """
    Runs the first round of the game
    """
    game_intro()
    get_player_battle_name()
    get_player_weapon_choice()
    get_enemy_battle_name()
    get_enemy_weapon()
    print_battle_outcome(player.players_battle_name, player.players_weapon)
    print_battle_outcome(player.enemys_battle_name, player.enemys_weapon)
    calculate_battle_results()
    score_board()
    play_again()


# color schemes (from colored https://pypi.org/project/colored/)
color_yellow = fg('#FFEB00')
color_blue = fg('#0035FF')
color_red = fg('#FF0000')
color_orange = fg('#FFA600')
color_green = fg('#00FF1A')
color_lightblue = fg('#00CFFF')
res = attr("reset")


# styling packages
hash_line = "#################################################################"
under_line = "________________________________________________________________"
text_box_rules = """_________________________________________________________________
|The ultimate alternative to the usual rock, paper and scissors.|
|Rules of the game: Nuclear Bomb kills human. Human kills       |
|cockroach. Cockroach survives the nuclear bomb.                |
|_______________________________________________________________|
"""


# weapons print art
C = """     ,--.     .--,
         /.".\,
    /\  /##|##\. /\.
   /  \{###|###}/  \.
 _/   {Cockroach}\. \_
    /  {###|###}  \.
    \   {##|##}   /
"""
NB = """   _.-^-....,,--.,
 -/  Nuclear Bomb \.
  ``--. . , ; .--''
    .-=|     |=-.
    `-=#$%&%$#=-'
       | ;  :|
 ___.,-#%&$@%#&#~,._____
"""
H = """  ////////
  |Human |
 {  o  o  }
  |  ^   |
   \ -- /
 ___|  |___
"""

# call functions to start game
player = Player()
main()
