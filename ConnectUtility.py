import SQLiteUtility as DB

COUNTER =0
ROW_COUNT = 6
COLUMN_COUNT = 7
MAX_COINS =42
DEBUG = True

matrix = [[0 for i in range(7)] for i in range(6)]
player1_actions = []
player2_actions = []


def check4Match(board, coin):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == coin and board[r][c + 1] == coin and board[r][c + 2] == coin and board[r][
                c + 3] == coin:
                if DEBUG:print(" ROW match")
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == coin and board[r + 1][c] == coin and board[r + 2][c] == coin and board[r + 3][
                c] == coin:
                if DEBUG:print("COL match")
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == coin and board[r + 1][c + 1] == coin and board[r + 2][c + 2] == coin and board[r + 3][
                c + 3] == coin:
                if DEBUG:print("Slope positive match")
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == coin and board[r - 1][c + 1] == coin and board[r - 2][c + 2] == coin and board[r - 3][
                c + 3] == coin:
                if DEBUG:print("Slope negative match")
                return True


def takeInput(game_id,position):
    coin = 1
    position -= 1
    global COUNTER
    if COUNTER % 2 == 0:
        coin = 1  # Yellow Coin
    else:
        coin = 2  # Red Coin
    # validating the boundries of game
    if position <= 6 and position >= 0:

        # Coins start placing from bottom of matrix
        last_row = 5
        while last_row>= 0:

            # if place is not occupied by any coin
            if matrix[last_row][position] == 0:
                matrix[last_row][position] = coin
                #if DEBUG:print("inserted")
                global player1_actions
                global player2_actions

                # Store player actions in global variables
                if coin==1:player1_actions.append(position+1)
                else:player2_actions.append(position+1)

                if DEBUG:displayMatrix()
                if check4Match(matrix, coin):
                    DB.init()
                    DB.createNewGame(game_id,player1_actions,player2_actions)
                    return f"{ 'Yellow' if coin==1 else 'Red'} won"
                break

            else:
                last_row -= 1
    else:
        return "Invalid"
        if DEBUG:print("Out of range")

    COUNTER -= 1
    return "Valid"

# Put zero values in the matrix
def reset():
    matrix = [[0 for i in range(7)] for i in range(6)]

# Interates the whole matrix
def displayMatrix():
    for i in range(0, 6):
        for j in range(0, 7):
            if DEBUG:print(matrix[i][j], end=' ')
        if DEBUG:print("\n")
    if DEBUG:print("-----------------")

def initialize():
    counter=0
    reset()

# if __name__ == "__main__":
#     print("READY")
#     initializeMatrix()
#     displayMatrix()
#     print(takeInput(10))
#     COUNTER = 0

