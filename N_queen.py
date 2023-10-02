def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if there is a queen in the same row
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        # Check upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Check lower diagonal on the left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(board, col):
        if col == n:
            result.append(["".join(row) for row in board])
            return

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                solve(board, col + 1)
                board[i][col] = '.'

    result = []
    empty_board = [['.' for _ in range(n)] for _ in range(n)]
    solve(empty_board, 0)
    return result

# Example usage for N = 4
solutions = solve_n_queens(4)
for solution in solutions:
    print(solution)
    print()


"""

Explanation:

solve_n_queens function initializes an empty chessboard and starts the backtracking process with the solve helper function.
The is_safe function checks if placing a queen at a given position is safe by examining the row, upper diagonal, and lower diagonal.
The solve function recursively explores possible placements for queens, backtracking when conflicts are detected or a solution is found.
The result is a list of all unique solutions, each represented as a list of strings (chessboard rows).

Time Complexity Analysis:
The time complexity of the N-Queens backtracking algorithm is exponential. In the worst case, it explores all possible configurations. Each queen placement decision results in branching, leading to a time complexity of O(N!) where N is the size of the chessboard.

"""
