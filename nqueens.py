import random as r
import time as t

# Implement a solver that returns a list of queen's locations
#  - Make sure the list is the right length, and uses the numbers from 0 .. BOARD_SIZE-1
def solve(board_size):

    # Reads the input file "nqueens.txt"
    f = open("input.txt", "r")
    if f.mode == "r":
        contents = f.read()

    # Creating the board.
    board = [[0 for col in range(board_size)] for row in range(board_size)]

    # Initial config of queens on board.
    for i in range(len(board)):
        # Row[elem]
        board[i][i] = 1

    print(board)    
    print(checkConflicts(0,0,board))  # Should be 3?

def minConflicts(board, steps):
    return True

# Checks to see if a board space is available
def checkConflicts(row, col, board):
    conflicts = 0
    # Checks row/column
    for i in range(len(board)):
        # Queen cannot conflict with itself
        if board[row][i] == 1 and col != i:
            conflicts += 1
        if board[i][col] == 1 and row != i:
            conflicts += 1
        
        # For diagonals
        for j in range(len(board)):
            if(row+col == i+j) or (row-col == i-j):
                if board[i][j] == 1 and (i != row and j != col):
                    conflicts += 1


    return conflicts

# Creates a new board with random placement of queens.
def randomShuffle(n):
    # Creates a new blank board
    board = [[0 for col in range(n)] for row in range(n)]

    # Place n queens
    for i in range(n):
        while True:
            row = r.randint(0,n-1)
            col = r.randint(0,n-1)

            if board[row][col] == 0:
                board[row][col] = 1
                break


    return board

def solution(board, boardSize):
    for x in range(1, boardSize + 1):
        for y in range(x + 1, boardSize + 1):
            if board[x-1] == board[y-1]:
                return False

    for i in range(1, boardSize + 1):
        j = i
        k = board[i - 1]
        while j < boardSize and k < boardSize:
            j = j + 1
            k = k + 1
            if board[j - 1] == k:
                return False
        j = i
        k = board[i - 1]
        while j < boardSize and k > 1:
            j = j + 1
            k = k - 1
            if board[j - 1] == k:
                return False
        j = i
        k = board[i - 1]
        while j > 1 and k < boardSize:
            j = j - 1
            k = k + 1
            if board[j - 1] == k:
                return False
        j = i
        k = board[i - 1]
        while j > 1 and k > 1:
            j = j - 1
            k = k - 1
            if board[j - 1] == k:
                return False
    return True

if __name__ == "__main__":
    solve(4)
