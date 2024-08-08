# Tic-Tac-Toe with Minimax AI

This project implements a classic Tic-Tac-Toe game using Python and Pygame, featuring an AI opponent that uses the Minimax algorithm for optimal play. The AI is designed to play perfectly, resulting in a tie with optimal play from both sides.

## Features

- **Play Against AI**: Challenge an AI opponent that uses the Minimax algorithm to determine the optimal move.
- **Player Choice**: Choose to play as 'X' or 'O'.
- **Game Status**: Displays game status including current player, game outcome (win/tie), and option to play again.
- **Graphical User Interface**: A user-friendly interface built with Pygame to handle game interactions and display.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/9Gaurav9/tictactoe.git
    ```

2. **Navigate to the Project Directory**:
    ```sh
    cd tictactoe
    ```

3. **Install Dependencies**:
    Make sure you have Python installed, then install the required packages:
    ```sh
    pip install pygame
    ```

## Usage

1. **Run the Game**:
    To start the game, execute:
    ```sh
    python runner.py
    ```

2. **Game Controls**:
    - **Player Choice**: Click on "Play as X" or "Play as O" to choose your player.
    - **Game Interaction**: Click on any empty cell to make a move when it's your turn.
    - **Play Again**: After the game ends, click on the "Play Again" button to restart.

## File Descriptions

- **`tictactoe.py`**: Contains the game logic including functions for game state management, move generation, and Minimax algorithm implementation.
- **`runner.py`**: Handles the game interface using Pygame, including user interactions and AI move processing.

## Functions Overview

- **`initial_state()`**: Returns the initial empty state of the Tic-Tac-Toe board.
- **`player(board)`**: Determines whose turn it is based on the current board state.
- **`actions(board)`**: Returns a set of possible moves for the current board state.
- **`result(board, action)`**: Returns a new board state resulting from a move.
- **`winner(board)`**: Checks for a winner on the board.
- **`terminal(board)`**: Checks if the game is over (win or tie).
- **`utility(board)`**: Provides the utility value of the board (1 for X win, -1 for O win, 0 for tie).
- **`minimax(board)`**: Determines the optimal move for the current player using the Minimax algorithm.

## Contributing

Feel free to contribute by creating issues or submitting pull requests. Contributions to improve the game or add new features are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


Enjoy playing Tic-Tac-Toe!
