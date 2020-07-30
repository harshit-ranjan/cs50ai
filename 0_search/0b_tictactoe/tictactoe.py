"""
Tic Tac Toe Player
"""

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
    X_count = 0
    O_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                X_count += 1
            elif cell == O:
                O_count += 1
    if X_count <= O_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acts = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                acts.add((i, j))
    return acts


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] == EMPTY:
        result_board = copy.deepcopy(board)
        result_board[i][j] = player(board)
        return result_board
    else:
        raise ValueError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] != None and all(elem == row[0] for elem in row):
            return row[0]

    if board[0][0] == board[1][0] == board[2][0] != None:
        return board[0][0]

    if board[0][1] == board[1][1] == board[2][1] != None:
        return board[0][1]

    if board[0][2] == board[1][2] == board[2][2] != None:
        return board[0][2]

    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[1][1]

    if board[2][0] == board[1][1] == board[0][2] != None:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -10  # Using -10 in place of -ve infinity
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    return v


def minvalue(board):
    if terminal(board):
        return utility(board)
    v = 10  # Using +10 in place of +ve infinity
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == [[EMPTY]*3]*3:
        return (0, 0)

    if terminal(board):
        return None

    if player(board) == X:
        v = -10
        for action in actions(board):
            mv = minvalue(result(board, action))
            if mv > v:
                sel_act = action
                v = mv
    else:
        v = 10
        for action in actions(board):
            mv = maxvalue(result(board, action))
            if mv < v:
                sel_act = action
                v = mv
    return sel_act
