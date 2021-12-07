import numpy as np

def hasWon(board):
    # A whole line or column sums up to -5 if all of its numbers were drawn 
    return -5 in board.sum(axis=0) or -5 in board.sum(axis=1)

def score(board,last):
    board[board == -1] = 0
    return last*board.sum()

# Part 1
def firstWinningBoard(boards,drawn):
    for number in drawn:
        for board in boards:
            board[board == number] = -1 # -1 replaces drawn numbers
            if hasWon(board):
                return score(board,number)

# Part 2
def lastWinningBoard(boards,drawn):
    for number in drawn:
        for board in boards:
            board[board == number] = -1
            if hasWon(board):
                if len(boards) > 1:
                    # Keep boards that have not won yet and continue
                    boards = [board for board in boards if not hasWon(board)]
                else:
                    return score(board,number)

# Read input data
with open("./Day4/input.txt") as f:
    data = f.read().splitlines()
    # Read order in which numbers are drawn
    marks = list(map(int,data.pop(0).split(",")))
    print(marks)
    data.pop(0)

    # Read all boards
    boards = []
    board = []
    for line in data:
        if len(line) < 2:
            board = np.asarray(board)
            boards.append(board)
            board = []
        else:
            board.append(list(map(int,line.split())))
    
    copy = boards.copy()
    print("Part 1 :",firstWinningBoard(boards,marks))
    print("Part 2 :",lastWinningBoard(copy,marks))