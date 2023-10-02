def matrix_chain_multiplication(matrices):
    n = len(matrices)
    
    # Initialize the cost matrix for dynamic programming
    cost = [[0] * n for _ in range(n)]

    # Initialize the parenthetical matrix to reconstruct the optimal solution
    parenthetical = [[0] * n for _ in range(n)]

    # Fill the cost matrix using dynamic programming
    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')
            for k in range(i, j):
                current_cost = cost[i][k] + cost[k + 1][j] + matrices[i - 1][0] * matrices[k][1] * matrices[j][1]
                if current_cost < cost[i][j]:
                    cost[i][j] = current_cost
                    parenthetical[i][j] = k

    # Reconstruct the optimal parenthesization
    def construct_parenthesization(i, j):
        if i == j:
            return f"M{i + 1}"
        else:
            k = parenthetical[i][j]
            left = construct_parenthesization(i, k)
            right = construct_parenthesization(k + 1, j)
            return f"({left} × {right})"

    parenthesization = construct_parenthesization(1, n - 1)

    return parenthesization, cost[1][n - 1]

# Example usage for matrices [(2, 3), (3, 4), (4, 2)]
matrices = [(2, 3), (3, 4), (4, 2)]
parenthesization, min_scalar_multiplications = matrix_chain_multiplication(matrices)

# Output results
print("Optimal Parenthesization:", parenthesization)
print("Minimum Scalar Multiplications:", min_scalar_multiplications)


"""

Explanation:

The matrix_chain_multiplication function initializes a cost matrix (cost) and a parenthetical matrix (parenthetical) for dynamic programming.
The dynamic programming algorithm fills in the cost matrix by considering all possible split points in the matrix chain.
The recurrence relation involves finding the optimal split point (k) that minimizes the total cost of multiplication.
The construct_parenthesization function is used to reconstruct the optimal parenthesization by recursively building the expression based on the split points.

Time and Space Complexity Analysis:

Time Complexity: O(n^3) where n is the number of matrices. This is because there are three nested loops used to fill the cost matrix.
Space Complexity: O(n^2) for storing the cost and parenthetical matrices.
Efficiency for Large Instances:

The dynamic programming approach is efficient for large instances of the matrix chain multiplication problem, thanks to its polynomial time complexity.

"""
