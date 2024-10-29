# Exploring Maximum Path Moves in a 2D Grid: Recursive and DP Strategies

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

- ## Using Memoization

    - ### Intuition
        - The problem requires determining the maximum number of valid moves in a grid, where a valid move consists of moving to an adjacent cell that has a strictly greater value than the current cell. The allowed movements are down-right, right, and up-right. The goal is to maximize the total number of such moves starting from any cell in the first column.

    - ### Approach
        1. **Recursive Traversal with Memoization**: Implement a recursive function `traverse` that explores possible moves from a given cell. The function checks if moving to an adjacent cell is valid (i.e., within bounds and has a strictly greater value). Results are cached to avoid redundant calculations.

        2. **Direction Handling**: The function attempts to move in three possible directions from the current cell, tracking the best number of subsequent valid moves.

        3. **Starting Points**: The traversal begins from each cell in the first column of the grid. For each starting position, the maximum moves are calculated using the `traverse` function.

        4. **Final Calculation**: The maximum moves obtained from all starting cells are returned, adjusted to account for counting moves instead of steps.

    - ### Time Complexity
        - The worst-case theoretical time complexity can be considered __O(3<sup>N</sup>)__, where __N__ is the number of rows, due to the branching factor of up to three recursive calls per cell.
        - However, practical scenarios usually lead to fewer unique paths due to the constraints of strictly increasing values, making the effective complexity closer to __O(N * M)__, where __M__ is the number of columns.

    - ### Space Complexity
        - The space complexity is __O(N)__ in the worst case due to the recursion stack. This occurs when the recursion goes as deep as the number of rows in the grid, especially in a scenario where each cell leads to a valid subsequent move.
        - Additionally, there is a cache used for memoization, which may also take __O(N * M)__ space in the worst case if all cells are stored.

    - ### Code
        ```python3 []
        class Solution:
            def maxMoves(self, grid: List[List[int]]) -> int:
                # Initialize variables to track the maximum moves and the dimensions of the grid
                max_Moves, total_Rows, total_Columns = 0, len(grid), len(grid[0])
                cache = {}  # Cache to store results of subproblems for memoization
                
                # Define the possible directions of movement: down-right, right, and up-right
                directions = [(-1, 1), (0, 1), (1, 1)]

                # Helper function to traverse the grid recursively
                def traverse(row: int, column: int, prev_No: int = -1):
                    # Base case: Check if the current position is out of bounds or not valid
                    if (row < 0 or row >= total_Rows or 
                        column < 0 or column >= total_Columns or 
                        grid[row][column] <= prev_No):
                        return 0  # Return 0 if the move is not valid
                    
                    # If the current position has not been computed before, calculate it
                    if (row, column) not in cache:
                        best_Choice = 0  # Initialize the best choice for the current position
                        
                        # Explore each possible direction
                        for dr, dc in directions:
                            # Recursively call traverse for the next position and update the best choice
                            best_Choice = max(best_Choice, traverse(row + dr, column + dc, grid[row][column]))
                        
                        # Store the result in cache for future reference
                        cache[(row, column)] = 1 + best_Choice  # Count this move + best subsequent moves
                    
                    # Return the cached result for the current position
                    return cache[(row, column)]

                # Start traversal from each row in the first column
                for row in range(total_Rows):
                    # Update max_Moves with the best result from each starting row
                    max_Moves = max(max_Moves, traverse(row, 0))

                # Return max_Moves adjusted by 1 (subtracting 1 since we count moves not steps)
                return max_Moves - 1 if max_Moves != 0 else 0
        ```

- ## Using Dynamic Programming

    - ### Intuition
        - The goal is to find the maximum number of moves that can be made in a grid, starting from any cell in the first column, while only moving to cells with strictly greater values in the specified directions (down-right, right, and up-right). We can utilize dynamic programming to efficiently compute the maximum moves for each cell by building upon previously computed results.

    - ## Approach
        1. **Dynamic Programming Table**: Create a DP table (`no_of_Moves`) where each cell represents the maximum number of moves that can be made starting from that cell.
        2. **Reverse Iteration**: Iterate through the grid from the second last column to the first column. This allows us to compute the maximum moves for each cell based on the adjacent cells in the next column.
        3. **Direction Exploration**: For each cell, check possible moves to adjacent cells. If the move is valid (the adjacent cell has a strictly greater value), update the DP table with the maximum moves possible.
        4. **Result Extraction**: After populating the DP table, find the maximum value in the first column, which represents the maximum moves starting from any cell in that column.

    - ### Time Complexity
        - **O(N * M)**: We iterate through each cell in the grid (N rows and M columns) and check a fixed number of directions (constant time operations), resulting in a linear complexity relative to the size of the grid.

    - ### Space Complexity
        - **O(N * M)**: The DP table requires storage proportional to the number of cells in the grid (N * M), where each entry stores the maximum moves from that cell.

    - ### Code
        ```python3 []
        class Solution:
            def maxMoves(self, grid: List[List[int]]) -> int:
                # Get the number of rows and columns in the grid
                total_Rows, total_Columns = len(grid), len(grid[0])
                
                # Define possible directions of movement: down-right, right, and up-right
                directions = [(-1, 1), (0, 1), (1, 1)]
                
                # Initialize a 2D list to store the number of moves from each cell
                no_of_Moves = [[0] * total_Columns for _ in range(total_Rows)]

                # Iterate through the grid in reverse order (bottom-up)
                for column in range(total_Columns - 2, -1, -1):
                    for row in range(total_Rows):
                        best_Choice = 0  # Initialize the best choice for the current position
                        
                        # Explore each possible direction
                        for dr, dc in directions:
                            new_row, new_column = row + dr, column + dc
                            
                            # Check if the next position is valid and has a strictly greater value
                            if (0 <= new_row < total_Rows and
                                0 <= new_column < total_Columns and
                                grid[new_row][new_column] > grid[row][column]):
                                best_Choice = max(best_Choice, 1 + no_of_Moves[row + dr][column + dc])
                        
                        # Store the best choice (maximum moves) for the current cell
                        no_of_Moves[row][column] = best_Choice

                max_Moves = 0  # Variable to track the maximum moves found
                # Iterate through the first column to find the maximum moves possible
                for row in range(total_Rows):
                    max_Moves = max(max_Moves, no_of_Moves[row][0])

                # Return the maximum moves found
                return max_Moves
        ```