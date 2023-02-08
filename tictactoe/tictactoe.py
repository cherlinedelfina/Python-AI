"""
Tic Tac Toe
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

"""
Returns player who has the next turn on a board.
"""
def player(board):
    X_count = 0
    O_count = 0

    # Count no of turns each player had
    for row in board:
        for col in row:
            if col == X:
                X_count += 1
            if col == O:
                O_count += 1

    #determine whose turn
    if X_count > O_count:
        return O
    else:
        return X


"""
Returns set of all possible actions (i, j) available on the board.
"""
def actions(board):
    avail_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                avail_actions.append([i, j])
    return avail_actions


"""
Returns the board that results from making move (i, j) on the board.
"""
def result(board, action):
    #deep copy board & add action
    boardcopy = copy.deepcopy(board)
    boardcopy[action[0]][action[1]] = player(boardcopy)
    return boardcopy


"""
Returns the winner of the game, if there is one.
"""
def winner(board):
    # check row
    for row in board:
        X_win = row.count(X)
        O_win = row.count(O)
        if X_win == 3:
            return X
        if O_win == 3:
            return O

    # check col
    cols = []
    for j in range(3):
        col = [row[j] for row in board]
        cols.append(col)

    for j in cols:
        X_win = j.count(X)
        O_win = j.count(O)
        if X_win == 3:
            return X
        if O_win == 3:
            return O

    # check diagonal
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

    # tie
    return None


"""
Returns True if game is over, False otherwise.
"""
def terminal(board):
    empty_counter = 0
    for row in board:
        empty_counter += row.count(EMPTY)

    if empty_counter == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False

"""
Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
"""
def utility(board):
    winners = winner(board)
    if winners == X:
        return 1
    elif winners == O:
        return -1
    else:
        return 0

"""
Returns the optimal action for the current player on the board.
"""
def minimax(board):
    current_player = player(board)

    if current_player == X:
        v = -math.inf
        for action in actions(board):
            k = min_value(result(board, action))
            if k > v:
                v = k
                best_move = action
    else:
        v = math.inf
        for action in actions(board):
            k = max_value(result(board, action))
            if k < v:
                v = k
                best_move = action
    return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v