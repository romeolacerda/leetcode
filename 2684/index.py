from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def dfs(r, c, grid, mem):
            if mem[r][c] != -1:
                return mem[r][c]

            max_moves = 0
            if r - 1 >= 0 and c + 1 < len(grid[0]) and grid[r - 1][c + 1] > grid[r][c]:
                max_moves = 1 + dfs(r - 1, c + 1, grid, mem)
            if c + 1 < len(grid[0]) and grid[r][c + 1] > grid[r][c]:
                max_moves = max(max_moves, 1 + dfs(r, c + 1, grid, mem))
            if r + 1 < len(grid) and c + 1 < len(grid[0]) and grid[r + 1][c + 1] > grid[r][c]:
                max_moves = max(max_moves, 1 + dfs(r + 1, c + 1, grid, mem))
            
            mem[r][c] = max_moves
            return max_moves

        rows = len(grid)
        cols = len(grid[0])
        mem = [[-1] * cols for _ in range(rows)]

        max_moves = 0
        for i in range(rows):
            max_moves = max(max_moves, dfs(i, 0, grid, mem))
        
        return max_moves
    
# example
grid = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
solution = Solution()
result = solution.maxMoves(grid)
print("Número máximo de movimentos:", result)