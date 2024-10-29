from typing import List

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