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

<a name="testing"></a>

## Testing

<a name="component-level-testing"></a>

### Component level Testing
- The website was tested and it is working on different browsers: Google Chrome, Firefox, and Microsoft Edge.

<a name="user-level-testing"></a>

### User level Testing
- Friends of mine tested the game for feedback. They reported that after a couple of rounds playing the game the terminal could get quite crowded and the text art to represent the different weapon objects were cut in half. To overcome this I have implemented a clear method to clear the terminal at every input stage of the user. 

<a name="bugs"></a>

### Bugs
While building the website some code was not behaving as expected. This happened mostly because of the order of functions being called and order in which variables were defined. Some other bugs I encountered were:

- I created the object player as part of the class Player. My idea was to first create the object and then slowly assign the values to it as the code/game runs. This was not possible because I was using the _init__ method. To make the adaptation I decided to use direct variables inside the class Player. 

- After deployment there was a bug that would append parts of my code to the top of the terminal even though I was using a clear method to clear the entire terminal. This was quite a difficult one to fix because this bug was not happening on my gitpod terminal. After a couple of hours on tutoring session, specially trying to replace the os clear method into different code lines to see if it would have any effect, we realized the bug was actually from the heroku terminal itself. I have then adapted the amount of rows available in the terminal deployed version for the code to run without any issues. 

<a name="validator-testing"></a>

### Validator Testing

- Python
    - No errors or warnings returned from the [PEP8 Online validator service](http://pep8online.com/)

<a name="accessibility"></a>

### Accessibility

- The colors used in some parts of the code displayed in the terminal were tested for good contrast on [WebAIM](https://webaim.org/resources/contrastchecker/)

<a name="deployment"></a>

## Deployment

The website was deployed using Heroku. For that, the following steps were taken:

1. All user input fields on the python code received a new line (\n) at the end of their input request.
2. Requirements were installed into the requirements.txt file using pip3 freeze > requirements.txt.
3. On Heroku’s main page clicked on 'New' and then 'Create New App'.
4. The project was given a unique name to match the GitHub repository and a region based on my location was selected. The project is then created by Heroku.
5.  With the project created, navigate to settings and add a config var with KEY input field ‘PORT’ and ‘VALUE’ input field 8000.
6. Scroll down right under the config var section and select to add a buildpack. A pop up window will open where I selected the Python icon, and then repeated the process to select the node.js buildpack. In this exact order so that the Python buildpack appears on top of the node.js buildpack.
7. Return to the deploy tab within the page and choose GitHub as your deploy method. This will require you to give Heroku access to your GitHub account. 
8. After connecting to GitHub, the name of the repository to be deployed is filled in and confirmed iby Heroku. 
9. The ‘Manual deploy’ method was selected as a way to keep track of changes and bugs that appear in the code. This allows you to also check the build of the app in an auto scroll window. 
10. After the deployment is complete, Heroku will display the message “Your app was successfully deployed.” And will provide a link to your live website. 
11. For any changes that happened in the code prior to the submission of this project, I updated the deployment manually using the main branch from GitHub.  
