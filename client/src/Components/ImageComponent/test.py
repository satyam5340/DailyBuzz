def solveSudoku(board):
    # Write your code here.

    ans = helper(board)
    print(ans)
    if ans:
        return board
    return -1


def helper(board):
    row, col = getNextEmpty(board)
    if row == 9:
        return True

    for i in range(1, 10):
        if isValid(i, board, row, col):
            board[row][col] = i
            if helper(board):
                return True
    board[row][col] = 0
    return False


def getNextEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return 9, 0


def isValid(i, board, row, col):
    for m in range(len(board)):
        if board[m][col] == i:
            return False
    for m in range(len(board[0])):
        if board[row][m] == i:
            return False
    startr = row - (row % 3)
    startc = col - (col % 3)
    for m in range(startr, startr + 3):
        for n in range(startc, startc + 3):
            if board[row][col] == i:
                return False
    return True