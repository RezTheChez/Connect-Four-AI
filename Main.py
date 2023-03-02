import numpy as np
import sys
import math
import pygame

gameOver = False
turn = 0
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

pygame.init()
font = pygame.font.SysFont("display", 75, bold = True)

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
            if board[row][col] == piece and board[row][col + 1] == piece and board[row][col + 2] == piece and board[row][col + 3] == piece:
                return True
    # Vertical ↕
    for col in range(boardCols):
        for row in range(boardRows - 3):
            if board[row][col] == piece and board[row + 1][col] == piece and board[row + 2][col] == piece and board[row + 3][col] == piece:
                return True

    # Positive Diagonals  ↗
    for col in range(boardCols - 3):
        for row in range(boardRows - 3):
            if board[row][col] == piece and board[row + 1][col + 1] == piece and board[row + 2][col + 2] == piece and board[row + 3][col + 3] == piece:
                return True

    # Negative Diagonals  ↖
    for col in range(boardCols - 3):
        for row in range(3, boardRows):
            if board[row][col] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece and board[row - 3][col + 3] == piece:
                return True

def drawBoard(board):
    for c in range(boardCols):
        for r in range(boardRows):
            pygame.draw.rect(screen, blueColor, (c * squareSize, r * squareSize + squareSize, squareSize, squareSize))
            pygame.draw.circle(screen, blackColor, (int(c * squareSize + squareSize / 2), int(r * squareSize + squareSize + squareSize / 2)), pieceRadius)

    for c in range(boardCols):
        for r in range(boardRows):
            if board[r][c] == 1:
                pygame.draw.circle(screen, yellowColor, (int(c * squareSize + squareSize / 2), screenHeight - int(r * squareSize + squareSize / 2)), pieceRadius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, redColor, (int(c * squareSize + squareSize / 2), screenHeight - int(r * squareSize + squareSize / 2)), pieceRadius)
    pygame.display.update()

def renderText(screen, color, text, xPos):
    label = font.render(text, 1, color)
    screen.blit(label, (xPos, 10))


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
                pygame.display.set_icon(screen)
                turn = 0

            elif event.key == pygame.K_1:
                if turn == 0:
                    row = findNextOpenRow(board, 0)
                    movePiece(board, row, 0, 1)
                    drawBoard(board)
                    turn = 1
                    
                    if winningMove(board, 1):
                        renderText(screen, yellowColor, "PLAYER 1 WINS!!!", 85)
                        gameOver = True
                else:
                    row = findNextOpenRow(board, 0)
                    movePiece(board, row, 0, 2)
                    drawBoard(board)
                    turn = 0
                    
                    if winningMove(board, 2):
                        renderText(screen, redColor, "PLAYER 2 WINS!!!", 85)
                        gameOver = True

            elif event.key == pygame.K_2:
                if turn == 0:
                    row = findNextOpenRow(board, 1)
                    movePiece(board, row, 1, 1)
                    drawBoard(board)
                    turn = 1
                    
                    if winningMove(board, 1):
                        renderText(screen, yellowColor, "PLAYER 1 WINS!!!", 85)
                        gameOver = True
                else:
                    row = findNextOpenRow(board, 1)
                    movePiece(board, row, 1, 2)
                    drawBoard(board)
                    turn = 0
                    
                    if winningMove(board, 2):
                        renderText(screen, redColor, "PLAYER 2 WINS!!!", 85)
                        gameOver = True

            elif event.key == pygame.K_3:
                if turn == 0:
                    row = findNextOpenRow(board, 2)
                    movePiece(board, row, 2, 1)
                    drawBoard(board)
                    turn = 1
                    
                    if winningMove(board, 1):
                        renderText(screen, yellowColor, "PLAYER 1 WINS!!!", 85)
                        gameOver = True
                else:
                    row = findNextOpenRow(board, 2)
                    movePiece(board, row, 2, 2)
                    drawBoard(board)
                    turn = 0
                    
                    if winningMove(board, 2):
                        renderText(screen, redColor, "PLAYER 2 WINS!!!", 85)
                        gameOver = True

            elif event.key == pygame.K_4:
                if turn == 0:
                    row = findNextOpenRow(board, 3)
                    movePiece(board, row, 3, 1)
                    drawBoard(board)
                    turn = 1
                    
                    if winningMove(board, 1):
                        renderText(screen, yellowColor, "PLAYER 1 WINS!!!", 85)
                        gameOver = True
                else:
                    row = findNextOpenRow(board, 3)
                    movePiece(board, row, 3, 2)
                    drawBoard(board)
                    turn = 0
                    
                    if winningMove(board, 2):
                        renderText(screen, redColor, "PLAYER 2 WINS!!!", 85)
                        gameOver = True

            elif event.key == pygame.K_5:
                if turn == 0:
                    row = findNextOpenRow(board, 4)
                    movePiece(board, row, 4, 1)
                    drawBoard(board)
                    turn = 1
                    
                    if winningMove(board, 1):
                        renderText(screen, yellowColor, "PLAYER 1 WINS!!!", 85)
                        gameOver = True
                else:
                    row = findNextOpenRow(board, 4)
                    movePiece(board, row, 4, 2)
                    drawBoard(board)
                    turn = 0
                    
                    if winningMove(board, 2):
                        renderText(screen, redColor, "PLAYER 2 WINS!!!", 85)
                        gameOver = True

            elif event.key == pygame.K_6:
                if turn == 0:
                    row = findNextOpenRow(board, 5)
                    movePiece(board, row, 5, 1)
                    drawBoard(board)
                    turn = 1
                    
                    if winningMove(board, 1):
                        renderText(screen, yellowColor, "PLAYER 1 WINS!!!", 85)
                        gameOver = True
                else:
                    row = findNextOpenRow(board, 5)
                    movePiece(board, row, 5, 2)
                    drawBoard(board)
                    turn = 0
                    
                    if winningMove(board, 2):
                        renderText(screen, redColor, "PLAYER 2 WINS!!!", 85)
                        gameOver = True

            elif event.key == pygame.K_7:
                if turn == 0:
                    row = findNextOpenRow(board, 6)
                    movePiece(board, row, 6, 1)
                    drawBoard(board)
                    turn = 1
                    
                    if winningMove(board, 1):
                        renderText(screen, yellowColor, "PLAYER 1 WINS!!!", 85)
                        gameOver = True
                else:
                    row = findNextOpenRow(board, 6)
                    movePiece(board, row, 6, 2)
                    drawBoard(board)
                    turn = 0
                    
                    if winningMove(board, 2):
                        renderText(screen, redColor, "PLAYER 2 WINS!!!", 85)
                        gameOver = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Player 1
            if turn == 0:
                # Getting Place To Move To
                mousePosX = event.pos[0]
                col = int(math.floor(mousePosX / squareSize))

                # Moving Piece
                if checkMove(board, col):
                    row = findNextOpenRow(board, col)
                    movePiece(board, row, col, 1)
                    pygame.display.set_icon(screen)

                    if winningMove(board, 1):
                        renderText(screen, yellowColor, "PLAYER 1 WINS!!!", 85)
                        gameOver = True
                drawBoard(board)

                # Changing Turns
                turn = 1
                print(np.flip(board, 0))

            # Player 2
            else:
                # Getting Place To Move To
                mousePosX = event.pos[0]
                col = int(math.floor(mousePosX / squareSize))

                # Moving Piece
                if checkMove(board, col):
                    row = findNextOpenRow(board, col)
                    movePiece(board, row, col, 2)
                    pygame.display.set_icon(screen)

                    if winningMove(board, 2):
                        renderText(screen, redColor, "PLAYER 2 WINS!!!", 85)
                        gameOver = True
                drawBoard(board)

                # Changing Turns
                turn = 0
                print(np.flip(board, 0))
            if gameOver:
                pygame.time.wait(3000)
