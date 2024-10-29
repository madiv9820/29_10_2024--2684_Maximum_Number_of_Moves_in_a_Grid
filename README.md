- ## Brute Force using Recursion (Time Limit Exceeded)

    - ### Intuition
        - The problem requires finding the maximum number of valid moves in a grid, where a valid move consists of moving to an adjacent cell that has a strictly greater value than the current cell. The movement is limited to three directions: down-right, right, and up-right. The goal is to maximize the total number of such moves starting from any cell in the first column.

    - ### Approach
        1. **Recursive Traversal**: Implement a recursive function `traverse` that explores possible moves from a given cell. The function checks if moving to an adjacent cell is valid (i.e., within bounds and has a strictly greater value).

        2. **Direction Handling**: The function attempts to move in three possible directions from the current cell, tracking the best number of subsequent valid moves.

        3. **Starting Points**: The traversal begins from each cell in the first column of the grid. For each starting position, the maximum moves are calculated using the `traverse` function.

        4. **Final Calculation**: The maximum moves obtained from all starting cells are returned, adjusted to account for counting moves instead of steps.

    - ### Time Complexity
        - The worst-case theoretical time complexity can be considered __O(3<sup>N</sup>)__, where __N__ is the number of rows, due to the branching factor of up to three recursive calls per cell.
        - However, practical scenarios usually lead to fewer unique paths due to the constraints of strictly increasing values, making the effective complexity closer to __O(N * M)__.

    - ### Space Complexity
        - The space complexity is __O(N)__ in the worst case due to the recursion stack. This occurs when the recursion goes as deep as the number of rows in the grid, especially in a scenario where each cell leads to a valid subsequent move.
    - ### Code
        ```python3 []
        class Solution:
            def maxMoves(self, grid: List[List[int]]) -> int:
                # Initialize variables to track the maximum moves and the dimensions of the grid
                max_Moves, total_Rows, total_Columns = 0, len(grid), len(grid[0])
                
                # Define the possible directions of movement: down-right, right, and up-right
                directions = [(-1, 1), (0, 1), (1, 1)]

                # Helper function to traverse the grid recursively
                def traverse(row: int, column: int, prev_No: int = -1):
                    # Base case: Check if the current position is out of bounds or not valid
                    if (row < 0 or  row >= total_Rows or 
                        column < 0 or column >= total_Columns or 
                        grid[row][column] <= prev_No):
                        return 0  # Return 0 if the move is not valid
                    
                    best_Choice = 0  # Initialize the best choice for the current position
                    
                    # Explore each possible direction
                    for dr, dc in directions:
                        # Recursively call traverse for the next position and update the best choice
                        best_Choice = max(best_Choice, traverse(row + dr, column + dc, grid[row][column]))
                    
                    return 1 + best_Choice # Return the count of moves (1 for the current move + best choice)

                # Start traversal from each row in the first column
                for row in range(total_Rows):
                    # Update max_Moves with the best result from each starting row
                    max_Moves = max(max_Moves, traverse(row, 0))

                # Return max_Moves adjusted by 1 (subtracting 1 since we count moves not steps)
                return max_Moves - 1 if max_Moves != 0 else 0
        ```