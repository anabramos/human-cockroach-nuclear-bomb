# Cockroaches & Nuclear Bomb

## About Cockroaches & Nuclear Bomb
Nuclear Bomb cockroaches is a back end browser game developed in Python. The game came to revolutionize the way we play rock, paper and scissors. 

Link to live website: [Cockroaches & Nuclear Bomb](https://cockroaches-nuclear-bombs.herokuapp.com/)



<a name="features"></a>

## Features

- Game Introduction section
    - The first section of the game introduces the user to the game, the objects of the game and its rules. It makes mention to the rock, paper and scissors game so that the user knows what to wait in terms of game format. 

- Battle name input
    - The game asks the user to log their battle name to start the game. The battle name can have a maximum of 20 characters and no spaces. If the battle name require spaces, this must be replaced by an underscore. 
    - Whenever a user inputs a battle name that is not valid (longer than 20 characters and/or with spaces) the game prints an error with an appropriate message. 
    - After the battle name is entered correctly the game affirms the validation of the game by printing a welcome message to the user. 

- Weapon choice input
    - The second user input field from the game will ask the user to pick their ‘weapon’ for the battle. The options are Human, Cockroach, and Nuclear Bomb. The user must type the capitalized initial(s) of each weapon to select the respective weapon for battle. 
    - If the character typed is not a valid one it will give an error message and repeat the instructions to provide a valid weapon choice.   
    - When the weapon choice is selected correctly and validated, it will immediately open the battle outcomes. 

- Enemy’s data
    - In the background, two functions are making sure to get a random name battle for the computer as well as a random weapon choice. 

- Battle floor
    - The battle floor will display the choice of both user (player) and computer (enemy) on the table with a small text art representing the choices respectively. 

- Battle outcome & Score Board
    - Under the battle floor the game will display the final result of this battle by telling the user if they have won, lost or if it was a tie.  
    - The score board will then designate a point to the appropriate winner of the battle.

- Play again question input  
    - After the first round of the battle the user will be asked if he would like to play another round. He is asked to type the capitalized initials of ‘ Y’  for yes and ‘N’ for no. 
    - An error will print in case the character types does not match the valid characters.
    - If the player types ‘Y’ the game will restart by only running the appropriate functions. This means the game will ask for the weapon choice of the play again and continue working with the same score, but will not ask for the player’s battle name again nor it will generate a new name for the enemy.
    - If the player types ‘N’ the game will end and print the overview of the battle(s) for the player. 

<a name="features-to-be-implemented"></a>

### Features to be implemented

- Implement a best of 3 or best of 5 game format where a player/enemy can play several rounds until the first scores 3 or 5 points – then the game will reset. 

- Display at the introduction to every new game (next to the instructions box) the battle name and score of the previous player.  
