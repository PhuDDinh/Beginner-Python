#This is a Tic Tac Toe game against a simple artificial intelligence, the AI will respond to the player's moves. 

import random

def drawBoard(board):
    # This function prints out the board.
    print("   |   |")
    print(" "  + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" "  + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" "  + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")

def inputPlayerLetter():
    # This function let the player type which letter they want to be. 
    # Return a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()
    
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"

def playAgain():
    # This function return True if the player wants to play again, otherwise it returns False.
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    # Given a board and a player's letter, this function returns True if that player has won.
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # this is across the top
    (board[4] == letter and board[5] == letter and board[6] == letter) or # this is across the middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or # this is across the bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or # this is down the left side
    (board[8] == letter and board[5] == letter and board[2] == letter) or # this is down the middle
    (board[9] == letter and board[6] == letter and board[3] == letter) or # this is down the right side
    (board[7] == letter and board[5] == letter and board[3] == letter) or # this is diagonal
    (board[9] == letter and board[5] == letter and board[1] == letter)) # this is diagonal

def getBoardCopy(board):
    # This function will make a duplicate of the board list and return the duplicate.
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    # Return True if the passed move is free on the passed board.
    return board[move] == " "

def getPlayerMove(board):
    # This function let the player type in their move.
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # This function returtn a valid move from the passed list on the passed board.
    # And return None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # This function is to determine the computer's move.
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"
    
    # Here is the algorithm for our AI:
    # First, check if we can win in the next move.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    # Check if the player could win in their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    # Checking the Corner, Center, and Side Spaces(in that order)
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5
    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # This function return True if every space on the board has been taken. Else return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print("Welcome to Tic Tac Toe!")

while True:
    # Reset the board
    theBoard = [" "] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("The {} will go first.".format(turn))
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "player":
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Hooray! You have won the game!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"
        
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("The computer has beaten you! You lose.")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = "player"
    if not playAgain():
        break




