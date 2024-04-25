def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print("_", end=" ")
        print()

def is_safe(board, row, col):
    # col check
    for i in range(col):
        if board[row][i] == 1:
            return False

    # upper diago check
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # lower diago check
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_N_Queen(board, col):
    # if all queens are placed
    if col >= N:
        return True

    # Place queen one by one
    for i in range(N):
        if is_safe(board, i, col):
            # Place the queen at board[i][col]
            board[i][col] = 1

            # pudhchi queen lavun bhg
            if solve_N_Queen(board, col + 1):
                return True

            # else remove the stack recursive call
            board[i][col] = 0

    return False

def solveNQ():
    global N
    N = int(input("Enter the size of the chessboard (N): "))
    board = [[0] * N for _ in range(N)]

    if solve_N_Queen(board, 0) is False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

if __name__ == '__main__':
    solveNQ()
