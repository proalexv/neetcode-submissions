class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Loop through each element of the grid, encoutner a one will cause a dfs where corresponding 1 -> 0, and a counter will track how many of those flips have occured. it will compared to a the max at the end and returned. 
        maxArea = 0 
        def dfs(grid, r, c):
            ROW, COLUMN = len(grid), len(grid[0])
           
            # Failure 
            if min(r,c) < 0 or r == ROW or c == COLUMN or grid[r][c] == 0: 
                return 0
            # Pass 
            if grid[r][c] == 1:
                grid[r][c] = 0
                return 1 + dfs(grid, r + 1, c)+ dfs(grid, r - 1, c)+ dfs(grid, r, c + 1,) + dfs(grid, r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(grid, r, c))
        
        return maxArea