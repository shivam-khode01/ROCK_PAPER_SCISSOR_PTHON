# ROCK_PAPER_SCISSOR_PTHON
An ols school hand game played by in early 20's. I tried to creats its virtual mode by using python . 

The code you provided is a Python program for playing a simple rock-paper-scissors game. Here's an explanation of the code:

Import the random module to generate computer choices randomly.

Initialize variables for keeping track of user, computer, and opponent wins.

Define emojis for the rock, paper, and scissors images.

Create a list called game_image containing the emojis for rock, paper, and scissors.

Prompt the user to input the number of rounds they want to play and their choice of game mode (multiplayer or against the computer).

If the user chooses multiplayer (user_input == 1), prompt for the second person's name.

Use a loop to play the specified number of rounds.

a. If user_input is 1 (multiplayer):

Prompt both players for their choices and display their chosen emojis.
Determine the winner of the round based on their choices and update the respective win counters (user_win or opponent_win).
Handle draws and invalid inputs.
b. If user_input is 2 (against the computer):

Prompt the user for their choice and generate a random choice for the computer.
Display the choices made by the user and the computer.
Determine the winner and update the win counters.
After all rounds are played, display the final scores and announce the winner (user or computer) for the respective game mode.

If the game mode is multiplayer (user_input == 1), the program also announces the winner between the user and their opponent.

Finally, there is a comment at the end of the code mentioning an explanation for GitHub README file, but it seems to be incomplete.
