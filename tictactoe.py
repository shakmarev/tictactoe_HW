"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    # If game is over return None.
    if terminal(board):
        return None
    # If X has more turns than O, it is O's turn.
    if sum(row.count(X) for row in board) > sum(row.count(O) for row in board):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # If game is over return None.
    if terminal(board):
        return None

    # If a certain cell is empty then it's valid move.
    acts = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                acts.add((i, j))

    return acts


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY or (i >= len(board) and j >= len(board)):
        raise Exception("Invalid action.")
    else:
        board_copy = deepcopy(board)
        board_copy[i][j] = player(board)
        return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # List of winning combinations.
    win_board = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]

    # Check if any line contains three same values.
    for row in win_board:
        if row.count(row[0]) == len(row) and row.count(EMPTY) == 0:
            return row[0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in (X, O):
        return True

    if any(EMPTY in row for row in board):
        return False
    else:
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
    # If the board is a terminal, the minimax function should return None.
    if terminal(board):
        return None

    if player(board) == X:
        v = -math.inf
        best_action = None

        # Pick an action 'a' that produces highest value of min values.
        for action in actions(board):
            min_val = minvalue(result(board, action))

            if min_val > v:
                v = min_val
                best_action = action

        return best_action

    elif player(board) == O:
        v = math.inf
        best_action = None

        # Pick an action 'a' that produces smallest value of max values.
        for action in actions(board):
            max_val = maxvalue(result(board, action))

            if max_val < v:
                v = max_val
                best_action = action

        return best_action


# Returns a value for maximizing player.
def maxvalue(board):
    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    return v


# Returns a value for minimizing player.
def minvalue(board):
    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
    return v
