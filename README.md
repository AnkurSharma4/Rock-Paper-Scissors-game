# Rock, Paper, Scissors Game

Welcome to the **Rock, Paper, Scissors Game**! This is a simple Python implementation of the classic hand game, where the user plays against the bot (computer). The user selects one of three options (Rock, Paper, or Scissors), and the bot randomly picks one as well. The game then determines the winner based on the rules of Rock, Paper, Scissors.

## Features

- **Player vs Bot:** The game pits the user against the computer (bot).
- **Random Bot Selection:** The bot's weapon is randomly chosen from the available options (Rock, Paper, or Scissors).
- **Game Outcome:** The game displays the result: whether the user wins, loses, or draws.
  
## Gameplay

1. **Start the Game:** The game will prompt you to choose your weapon (Rock, Paper, or Scissors).
2. **Bot's Move:** After you make your selection, the bot will randomly choose one of the three weapons.
3. **Game Result:** The program will compare your choice to the bot's and declare a winner or if the game is a draw.

## How to Run the Program

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `rock_paper_scissors.py` file is located.
4. Run the game using Python:
   ```bash
   python rock_paper_scissors.py
   ```

5. Follow the on-screen prompts to play the game.

## Example Gameplay

```
The Rock, Paper, Scissors Game
['Rock', 'Paper', 'Scissors']
enter your weapon: Rock
user chose Rock, bot chose Paper
Bot Wins....
```

In this example:
- The user selects "Rock".
- The bot randomly selects "Paper".
- The program compares the selections and prints the outcome: "Bot Wins....".

Another example:

```
The Rock, Paper, Scissors Game
['Rock', 'Paper', 'Scissors']
enter your weapon: Scissors
user chose Scissors, bot chose Rock
Bot Wins....
```

In this case:
- The user selects "Scissors".
- The bot randomly selects "Rock".
- The program announces "Bot Wins....".

Or if it's a draw:

```
The Rock, Paper, Scissors Game
['Rock', 'Paper', 'Scissors']
enter your weapon: Paper
user chose Paper, bot chose Paper
same weapons collapsed! It's a Draw
```

In this case:
- The user selects "Paper".
- The bot randomly selects "Paper".
- The result is a draw.

## Code Breakdown

1. **Weapon Selection:** The program first shows the available weapons (Rock, Paper, and Scissors).
2. **User Input:** The user is prompted to input their weapon choice.
3. **Bot Selection:** The bot randomly selects one of the three weapons using `random.choice()`.
4. **Result Comparison:** The program compares the user's choice and the bot's choice to determine the winner or if it is a draw.
   - **Rock beats Scissors.**
   - **Scissors beats Paper.**
   - **Paper beats Rock.**
   - If both the user and bot select the same weapon, it is a draw.

## Requirements

- **Python 3.x** is required to run the program.
- No additional libraries are required since it only uses the `random` module.

## How to Contribute

1. Fork the repository to your own GitHub account.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Submit a pull request describing your changes.

## License

This project is licensed under the MIT License.

---

This README provides a clear, interactive overview of how to play the game, run it, and what each part of the code does. It also includes example gameplay to make it easy for users to understand how the program works when they run it.
