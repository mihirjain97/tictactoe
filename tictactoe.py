# BOard D
# display Board D
# play game
# check win
# check rows
# check columns
# check diagnols
# check tie
# Flip Player

# ----------Global Variables -----

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if Game is Still goin on
gameIsOn = True

# Who won
winner = None

# current Player
currentPlayer = "X"

# This function used to display the Game Board

# Display Board


def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Main function to play game


def playGame():

    # display the board
    displayBoard()

    while gameIsOn:

        # Function created for the display of X and O on the board
        handleTurn(currentPlayer)

        # Check if the game has ended
        checkIfGameOver()

        # to change or flip the player
        flipPlayer()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


def handleTurn(currentPlayer):
    # choosing the position and accordingly playing the game
    # eg. if position = 1, then on the 1st position of board
    # X or O will be displayed on 1st position of the board

    position = input(currentPlayer + "'s Turn: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose your input again." +
                             "\n" + currentPlayer + "'s Turn: ")
        position = int(position) - 1

        # Check position empty or not

        if board[position] == "-":
            valid = True
        else:
            print("Position Already Occupied. Please change the position.")

    board[position] = currentPlayer

    displayBoard()


def checkIfGameOver():
    checkForWinner()
    checkIfTie()


def checkForWinner():

    # Set up global variables
    global winner

    # check rows
    rowWinner = checkRows()
    # check columns
    columnWinner = checkColumns()
    # check Diagnols
    diagnolWinner = checkDiagnols()

    if rowWinner:
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagnolWinner:
        winner = diagnolWinner
    else:
        winner = None
    return


def checkRows():
    # Set up global variables
    global gameIsOn
    # check if any of the rows have all the same value & is not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        gameIsOn = False
        # Return the winner (X or O)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def checkColumns():
    # Set up global variables
    global gameIsOn
    # check if any of the column have all the same value & is not empty
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        gameIsOn = False
        # Return the winner (X or O)
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return


def checkDiagnols():
    # Set up global variables
    global gameIsOn
    # check if any of the Diagnol have all the same value & is not empty
    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[6] == board[4] == board[2] != "-"
    if dia_1 or dia_2:
        gameIsOn = False
        # Return the winner (X or O)
    if dia_1:
        return board[0]
    if dia_2:
        return board[6]
    return


def checkIfTie():
    # Global variable we need
    global gameIsOn
    if "-" not in board:
        gameIsOn = False
    return


def flipPlayer():
    # Global Variable we need
    global currentPlayer
    # If the current player was X, then change it to O
    if currentPlayer == "X":
        currentPlayer = "O"
    # If the current player was O, then change it to X
    elif currentPlayer == "O":
        currentPlayer = "X"
    return


play = input("Do you wanna Play Game?  ")
if play == 'Y' or play == 'y':
    playGame()
else:
    exit
