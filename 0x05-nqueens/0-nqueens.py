#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Check if a queen can be placed at board[row][col]
    without attacking any other queens
    """

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_util(N, board, 0, solutions)
    return solutions

def solve_util(N, board, col, solutions):
    # Base case: all queens are placed
    if col == N:
        solution = [''.join('Q' if cell == 1 else '.' for cell in row) for row in board]
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_util(N, board, col + 1, solutions)
            board[i][col] = 0

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            raise ValueError
    except ValueError:
        print("N must be a number and at least 4.")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print('\n'.join(solution))
        print()

if __name__ == "__main__":
    main()

