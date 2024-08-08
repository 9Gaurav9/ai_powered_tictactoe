import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of Xs and Os on the board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # If X's count is greater than O's count, it's O's turn, otherwise it's X's turn
    if x_count > o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available_actions.add((i, j))

    return available_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    # Ensure the action is valid
    if board[i][j] is not EMPTY:
        raise Exception("Invalid move")

    # Create a deep copy of the board to ensure the original is not modified
    new_board = copy.deepcopy(board)

    # Set the cell to the player's mark
    new_board[i][j] = player(board)

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If there's a winner, the game is over
    if winner(board) is not None:
        return True

    # If there are no empty spaces left, the game is over (tie)
    for row in board:
        if EMPTY in row:
            return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        value, best_action = max_value(board)
    else:
        value, best_action = min_value(board)

    return best_action

def max_value(board):
    """
    Returns the maximum utility value possible and the corresponding action for X.
    """
    if terminal(board):
        return utility(board), None

    value = -math.inf
    best_action = None

    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > value:
            value = min_val
            best_action = action

    return value, best_action

def min_value(board):
    """
    Returns the minimum utility value possible and the corresponding action for O.
    """
    if terminal(board):
        return utility(board), None

    value = math.inf
    best_action = None

    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < value:
            value = max_val
            best_action = action

    return value, best_action