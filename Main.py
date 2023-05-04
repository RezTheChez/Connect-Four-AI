import numpy as np
import sys
import math
import pygame
import random
import time

from aiplayer import *

gameOver = False
turn = 1
player = 0
boardRows = 6
boardCols = 7
squareSize = 100
screenWidth = boardCols * squareSize
screenHeight = (boardRows + 1) * squareSize
screenSize = (screenWidth, screenHeight)
redColor = (255, 0, 0)
yellowColor = (255, 255, 0)
blueColor = (0, 0, 255)
blackColor = (0, 0, 0)
pieceRadius = int(squareSize / 2 - 5)
windowLength = 4
totalMoves = 0
defaultDepth = 4

empty = 0
player = 1
ai = 2

pygame.init()
font = pygame.font.SysFont("display", 75, bold=True)

# Initialize Board
def createBoard():
    board = np.zeros((boardRows, boardCols))
    return board


def movePiece(board, row, col, piece):
    board[row][col] = piece


def checkMove(board, col):
    return board[boardRows - 1][col] == 0


def findNextOpenRow(board, col):
    for row in range(boardRows):
        if board[row][col] == 0:
            return row


def winningMove(board, piece):
    # Horizontal ↔
    for col in range(boardCols - 3):
        for row in range(boardRows):
            if board[row][col] == piece and board[row][col + 1] == piece and board[row][col + 2] == piece and \
                    board[row][col + 3] == piece:
                return True
    # Vertical ↕
    for col in range(boardCols):
        for row in range(boardRows - 3):
            if board[row][col] == piece and board[row + 1][col] == piece and board[row + 2][col] == piece and \
                    board[row + 3][col] == piece:
                return True

    # Positive Diagonals  ↗
    for col in range(boardCols - 3):
        for row in range(boardRows - 3):
            if board[row][col] == piece and board[row + 1][col + 1] == piece and board[row + 2][col + 2] == piece and \
                    board[row + 3][col + 3] == piece:
                return True

    # Negative Diagonals  ↖
    for col in range(boardCols - 3):
        for row in range(3, boardRows):
            if board[row][col] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece and \
                    board[row - 3][col + 3] == piece:
                return True

def getValidLocations(board):
	validLocations = []
	for col in range(boardCols):
		if checkMove(board, col):
			validLocations.append(col)
	return validLocations


def evaluateWindow(window, piece):
    score = 0
    opposingPiece = player

    if piece == player:
        opposingPiece = ai

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(empty) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(empty) == 2:
        score += 2

    if window.count(opposingPiece) == 4:
        score -= 100
    elif window.count(opposingPiece) == 3 and window.count(empty) == 1:
        score -= 5
    elif window.count(opposingPiece) == 2 and window.count(empty) == 2:
        score -= 2

    return score


def evaluateBoard(board, piece):
    score = 0

    # Score center col because the center is the most important col on the board
    centerArray = [int(i) for i in list(board[:, boardCols // 2])]
    leftArray = [int(i) for i in list(board[:, boardCols // 2 - 1])]
    rightArray = [int(i) for i in list(board[:, boardCols // 2 + 1])]
    centerCount = centerArray.count(piece)
    leftCount = leftArray.count(piece)
    rightCount = rightArray.count(piece)
    score += centerCount * 2
    score += leftCount * 1
    score += rightCount * 1

    # Score horizontal
    for r in range(boardRows):
        rowArray = [int(i) for i in list(board[r, :])]
        for c in range(boardCols - 3):
            window = rowArray[c: c + windowLength]
            score += evaluateWindow(window, piece)

    # Score vertical
    for c in range(boardCols):
        colArray = [int(i) for i in list(board[:, c])]
        for r in range(boardRows - 3):
            window = colArray[r: r + windowLength]
            score += evaluateWindow(window, piece)

    # Score posiive sloped diagonal
    for r in range(boardRows - 3):
        for c in range(boardCols - 3):
            window = [board[r + i][c + i] for i in range(windowLength)]
            score += evaluateWindow(window, piece)

    for r in range(boardRows - 3):
        for c in range(boardCols - 3):
            window = [board[r + 3 - i][c + i] for i in range(windowLength)]
            score += evaluateWindow(window, piece)

    return score


def minimax(board, depth, piece):
    score = 0
    opposingPiece = player
    validLocations = getValidLocations(board)

    if piece == player:
        opposingPiece = ai

    if winningMove(board, piece) or winningMove(board, opposingPiece) or len(getValidLocations(board)) == 0 or depth == 0:
        if len(getValidLocations(board)) == 0:
            return None, 0
        else:
            return None, evaluateBoard(board, player)  # Always evaluate player
    else:
        if piece == ai:
            score = 1000
            boardCopy = np.copy(board)
            column = random.choice(validLocations)


            for col in validLocations:
                boardCopy2 = np.copy(boardCopy)
                row = findNextOpenRow(board, col)
                movePiece(boardCopy2, row, col, ai)
                newScore = minimax(boardCopy2, depth - 1, player)[1]

                if newScore < score:
                    score = newScore
                    column = col

                score = min(newScore, score)
            return column, score
        else:
            score = -1000
            boardCopy = np.copy(board)
            column = random.choice(validLocations)

            for col in validLocations:
                boardCopy2 = np.copy(boardCopy)
                row = findNextOpenRow(board, col)
                movePiece(boardCopy2, row, col, player)
                newScore = minimax(boardCopy2, depth - 1, ai)[1]

                if newScore > score:
                    score = newScore
                    column = col

                score = max(newScore, score)

            return column, score

def calculateEvaluation(piece):
    eval = minimax(board, depth, player)[2]

    if eval >= 0:
        eval = "+" + str(eval)
    else:
        eval = str(eval)

    return "Board evaluation: " + eval

def drawBoard(board):
    for c in range(boardCols):
        for r in range(boardRows):
            pygame.draw.rect(screen, blueColor, (c * squareSize, r * squareSize + squareSize, squareSize, squareSize))
            pygame.draw.circle(screen, blackColor, (
            int(c * squareSize + squareSize / 2), int(r * squareSize + squareSize + squareSize / 2)), pieceRadius)

    for c in range(boardCols):
        for r in range(boardRows):
            if board[r][c] == 1:
                pygame.draw.circle(screen, yellowColor, (
                int(c * squareSize + squareSize / 2), screenHeight - int(r * squareSize + squareSize / 2)), pieceRadius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, redColor, (
                int(c * squareSize + squareSize / 2), screenHeight - int(r * squareSize + squareSize / 2)), pieceRadius)
    pygame.display.update()


def renderText(screen, color, text, xPos):
    label = font.render(text, 1, color)
    screen.blit(label, (xPos, 10))

#def endGame(screen, gameOver):
#    gameOver = True
 #   renderText(screen, yellowColor, "PLAYER 1 WINS!!!", 85)
  #  pygame.time.wait(3000)
   # sys.exit()



board = createBoard()
screen = pygame.display.set_mode(screenSize)
drawBoard(board)

# Main Loop
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board = np.zeros((boardRows, boardCols))
                turn = 0
                drawBoard(board)

        elif event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, blackColor, (0, 0, screenWidth, squareSize))
            posx = event.pos[0]
            if turn == 2:
                pygame.draw.circle(screen, redColor, (posx, int(squareSize / 2)), pieceRadius)
            else:
                pygame.draw.circle(screen, yellowColor, (posx, int(squareSize / 2)), pieceRadius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Player 1
            if turn == player:
                pygame.draw.rect(screen, blackColor, (0, 0, screenWidth, squareSize))
                # Getting Place To Move To
                mousePosX = event.pos[0]
                col = int(math.floor(mousePosX / squareSize))

                # Moving Piece
                if checkMove(board, col):
                    row = findNextOpenRow(board, col)
                    movePiece(board, row, col, 1)

                    if winningMove(board, 1):
                        renderText(screen, yellowColor, "PLAYER 1 WINS!!!", 85)
                        gameOver = True

                drawBoard(board)

                # Changing Turns
                turn = 2
                #print(np.flip(board, 0))
                print(calculateEvaluation(defaultDepth, player))

            # Player 2
            if turn == ai and not gameOver:
                pygame.draw.rect(screen, blackColor, (0, 0, screenWidth, squareSize))
                # Getting Place To Move To
                mousePosX = event.pos[0]
                col, eval = minimax(board, defaultDepth, ai)

                # Moving Piece
                if checkMove(board, col):
                    row = findNextOpenRow(board, col)
                    movePiece(board, row, col, ai)

                    if winningMove(board, ai):
                           renderText(screen, redColor, "PLAYER 2 WINS!!!", 85)
                           gameOver = True
                    drawBoard(board)

                    # Changing Turns
                    turn = 1
                    #print(np.flip(board, 0))
    if gameOver:
        gameOver = True
        renderText(screen, yellowColor, "PLAYER 1 WINS!!!", 85)
        pygame.time.wait(3000)
        sys.exit()
