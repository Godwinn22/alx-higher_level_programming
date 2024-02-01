#!/usr/bin/python3

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve(board, row):
        if row == N:
            solutions.append([(i, row) for i in range(N) if board[i][row] == 1])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[col][row] = 1
                solve(board, row + 1)
                board[col][row] = 0

    solve(board, 0)

    for solution in solutions:
        print(solution)