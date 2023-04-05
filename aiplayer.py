# Guided AI code file

# In the next few weeks, let's work on the heuristic function and
# fundamental minimax logic of the AI player! Once you have the logic 
# implemented, you can experiment with different heuristics and search depths
# to see what works best for your AI. If you have extra time, you can also
# re-implement minimax with alpha-beta pruning to increase your AI's
# compute speed.

# I've outlined each function below, along with its purpose, parameters, and
# return values. Before you begin coding, I highly recommend watching the YouTube 
# video below explaining how the evaluation function, minimax, and alpha-beta pruning 
# conceptually work together in a chess game example. It also walks through some 
# great pseudocode that you can use as a starting point. I've pasted in the pseudocode
# for the minimax and minimax with alpha-beta pruning algorithms below for your convenience.
# https://www.youtube.com/watch?v=l-hh51ncgDI

# You can call these functions from main.py adding "from aiplayer import *" at the top
# of the file. https://www.geeksforgeeks.org/python-call-function-from-another-file/

# If you have any questions or concerns, feel free to email me at zen.thpk@berkeley.edu

# Good luck, and see you again soon! 


def possible_board_states(board_state, is_ai_player):
    
    """
    Returns a list of possible board states based on whose turn it is.
    Should be used in minimax(), minimax_with_pruning(), and find_best_ai_move().
    ---
    Parameters 
    - board_state: a 2D array representing the current board 
    - is_ai_player: boolean (true or false) indicating whether it is the AI's turn
    Returns
    - possible_states: list of 2D arrays representing possible board states after 
        the current player's move 
    
    """
    
    return possible_states


def evaluate_board(board):

    """
    This is our evaluation function, to be used in minimax() and minimax_with_pruning().
    Assign a positive score if the board is a "good" state for our human player.
    Assign a negative score if the board is a "good" state for our AI player.

    How you define "good" is challenging, but for starters a win state for the human 
    should return a very large positive number (e.g. 99999) while a win state 
    for the AI should return a very large negative number (e.g. -99999).
    A draw should return a 0. All other board states should return some number
    between the large positive and negative number.

    Things to consider designing the heuristic:
    - Can the AI player win with their next stone? 
      How many possible ways could the AI player win with their next stone?
    - How many open 3 in a rows does the AI player have? 
      How many more stones would the AI player need to fill in the fourth stone in the row?
    - Is the board approaching a draw state? Are there any possible wins remaining for 
      each player?
    - How can we anticipate and prevent direct losing moves? How does the AI block the human 
      player or avoid helping the human win?

    Experiment with different heuristics to see how smart your AI's plays are.
    ---
    Parameters
    - board: a 2D array representing the board to be scored
    Returns
    - score: a positive or negative integer for the board

    """

    return score


def minimax(board, depth, is_ai_player):

    """
    This function defines the logic of minimax.
    Minimax assumes the human player will always select moves maximizing the board score,
    while the AI player always moves to minimize the board score.
    
    The purpose of the minimax algorithm is to return the score of the provided board.
    It does so by scoring all the possible board states reachable within the provided search
    depth and returns the best score that would result if the human and AI player took turns 
    maximizing and minimizing the score.
    
    The next function, find_best_ai_move(), calls minimax() to score all of the board states
    reachable in the next AI move, allowing the AI to decide where to place its next stone.

    Video Walkthrough: https://www.youtube.com/watch?v=KU9Ch59-4vw  
    ---
    Parameters
    board: a 2D array representing a possible board state
    depth: the remaining levels of depth left to search, which decreases by 1 each time minimax()
        calls itself
    is_ai_player: boolean (true or false) indicating whether it is the AI's turn. Should become 
        the opposite value each time minimax calls itself.
    Returns
    best_score: the best score after running the minimax algorithm

    """

    # Pseudocode
    # if depth == 0 or game over in board
	#	return static evaluation of board
	# if humanPlayer
	# 	maxEval = -infinity
	# 	for each child of board
	# 		eval = minimax(child, depth - 1, true)
	# 		maxEval = max(maxEval, eval)
    #   best_score = maxEval
	# else
	# 	minEval = +infinity
	# 	for each child of board
	# 		eval = minimax(child, depth - 1, false)
	# 		minEval = min(minEval, eval)
    #   best_score = minEval
    
    return best_score


def find_best_ai_move(board, search_depth):
    
    """
    Determines the AI's next move by running minimax() on all board states reachable 
    in the next AI move, and returning the one with the best (most negative) score.
    
    Experiment with different search_depths and select one that allows the AI to make 
    a reasonably smart but quick decision. The greater the depth, the longer it will 
    take for the AI to compute its next move.

    This function should be called by your game logic whenever it is the AI's turn.
    ---
    Parameters
    board: 2D array representing the current board state
    search_depth: the depth you'd like the minimax algorithm to search to, i.e. how many
        times you'd allow minimax to call itself
    Returns
    best_move: the coordinates of the AI's next move

    """

    return best_move




### IF YOU HAVE EXTRA TIME, TRY THESE OPTIMIZATIONS ###
# Only start on these once you get the basic heuristic and minimax logic working.

def minimax_with_pruning(board, depth, alpha, beta, is_ai_player):

    """
    This function reimplements the logic of minimax with alpha-beta pruning.
    Alpha-beta pruning helps the AI cut out certain board states from 
    consideration by assuming that both players always move towards the board
    state with its optimal score. Since there are less possible board states to 
    explore and score, the computation time of minimax is reduced, allowing us
    to potentially increase the search depth of the AI.

    Explanation: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
    Video walkthrough: https://www.youtube.com/watch?v=xBXHtz4Gbdo

    """

    # Pseudocode
	# if depth == 0 or game over in board
	# 	return static evaluation of board
	# if humanPlayer
	# 	maxEval = -infinity
	# 	for each child of board
	# 		eval = minimax(child, depth - 1, alpha, beta, true)
	# 		maxEval = max(maxEval, eval)
	# 		alpha = max(alpha, eval)
	# 		if beta <= alpha
	# 			break
	# 	best_score = max_Eval
	# else
	# 	minEval = +infinity
	# 	for each child of board
	# 		eval = minimax(child, depth - 1, alpha, beta, false)
	# 		minEval = min(minEval, eval)
	# 		beta = min(beta, eval)
	# 		if beta <= alpha
	# 			break
	# 	best_score = minEval

    return best_score

# If you have even more time, try implementing these other optimizations from
# this guide, starting from chapter 5. The simplest to implement first are 
# optimizations covered in chapter 5 and 9.
# http://blog.gamesolver.org/solving-connect-four/05-move-exploration-order/

# You can also try prolonging the game if the AI is losing and shortening the game
# if the AI is winning by keeping track of search depth and adding/subtracting it
# from the winning/losing score:

# Pseudocode
# if human has won:
#    return 99999 – depth
# else if AI has won:
#    return -99999 + depth

# To check if these optimizations are working, time your AI to see if it is
# making its decisions more quickly and have it play against different people
# to see if it is effectively countering different play strategies.

# After we're done with all this, we can move on to the other fun features - 
# difficulty levels, leaderboards, website hosting, and more! :)
