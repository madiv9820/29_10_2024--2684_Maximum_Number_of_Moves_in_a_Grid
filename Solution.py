from typing import List

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