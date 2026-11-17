class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if we reach water, we might not care 
        # if we reach an island, we check surrounding elements for water
        # if it another island, check ikf that has water surroudning it
        
        islands = 0 
        ROW, COLUMN  = len(grid), len(grid[0])
        def dfs (grid, r, c) :
            if min(r,c) < 0  or r == ROW or c == COLUMN or grid[r][c] != "1": 
                return 
            
            elif grid[r][c] == "1":
                grid[r][c] = 0 
                dfs (grid, r + 1, c)
                dfs (grid, r - 1, c)
                dfs (grid, r, c + 1)
                dfs (grid, r, c - 1)

            # Loop through each elements 
            
        for x in range(ROW):
            for y in range(COLUMN):
                if grid[x][y] == "1": 
                    islands += 1
                    dfs(grid, x, y)
        return islands





