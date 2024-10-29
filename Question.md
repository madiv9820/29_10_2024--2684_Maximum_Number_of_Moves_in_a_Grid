# 2684. Maximum Number of Moves in a Grid

__Type:__ Medium <br>
__Topics:__ Array, Dynamic Programming, Matrix <br>
__Companies:__ Amazon <br>
__Leetcode Link:__ [Maximum Number of Moves in a Grid](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid)
<hr>

You are given a __0-indexed__ `m x n` matrix `grid` consisting of __positive__ integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

- From a cell `(row, col)`, you can move to any of the cells: `(row - 1, col + 1)`, `(row, col + 1)` and `(row + 1, col + 1)` such that the value of the cell you move to, should be __strictly__ bigger than the value of the current cell.

Return _the **maximum** number of **moves** that you can perform._
<hr>

### Examples

- __Example 1:__ <br>
![](https://assets.leetcode.com/uploads/2023/04/11/yetgriddrawio-10.png) <br>
__Input:__ grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]] <br>
__Output:__ 3 <br>
__Explanation:__ We can start at the cell (0, 0) and make the following moves: 
<br> - (0, 0) -> (0, 1). 
<br> - (0, 1) -> (1, 2). 
<br> - (1, 2) -> (2, 3). <br>
It can be shown that it is the maximum number of moves that can be made.

- __Example 2:__ <br>
![](https://assets.leetcode.com/uploads/2023/04/12/yetgrid4drawio.png) <br>
__Input:__ grid = [[3,2,4],[2,1,9],[1,1,7]] <br>
__Output:__ 0 <br>
__Explanation:__ Starting from any cell in the first column we cannot perform any moves.
<hr>

### Constraints:

- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 1000`
- <code>4 <= m * n <= 10<sup>5</sup></code>
- <code>1 <= grid[i][j] <= 10<sup>6</sup></code>
<hr>

### Hints
- Consider using dynamic programming to find the maximum number of moves that can be made from each cell.
- The final answer will be the maximum value in cells of the first column.