"""
Tic Tac Toe Player
"""

import math

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
    x_count = sum([row.count(X) for row in board])
    o_count = sum([row.count(O) for row in board])
    
    if x_count > o_count:
        return O
    return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    new_board = [row[:] for row in board]  # Deep copy of the board
    current_player = player(board)
    new_board[i][j] = current_player
    return new_board
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(board[i][j] != EMPTY for i in range(3) for j in range(3))
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None  # No action to take if the game is over
    
    current_player = player(board)
    
    if current_player == X:
        # Maximize for X
        best_score = -math.inf
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_score(new_board)
            if score > best_score:
                best_score = score
                best_move = action
        return best_move
    else:
        # Minimize for O
        best_score = math.inf
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_score(new_board)
            if score < best_score:
                best_score = score
                best_move = action
        return best_move

def minimax_score(board):
    if terminal(board):
        return utility(board)
    
    current_player = player(board)
    if current_player == X:
        best_score = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_score(new_board)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_score(new_board)
            best_score = min(best_score, score)
        return best_score
    # raise NotImplementedError
