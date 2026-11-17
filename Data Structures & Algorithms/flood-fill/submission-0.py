class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        strt_color = image[sr][sc]
        
        def dfs(grid, r, c, color, vist):
            COLUMN, ROW = len(grid[0]), len(grid)

            # Base cases for failure
            if min(r,c) < 0 or r == ROW or c == COLUMN or (r,c) in vist or grid[r][c] != strt_color:
                return 
            # Base case for acceptance 
            if grid[r][c] == strt_color:
                grid[r][c] = color 
            
            vist.add((r,c))
            
         
            dfs(grid, r + 1, c, color, vist)
            dfs(grid, r - 1, c, color, vist)
            dfs(grid, r, c + 1 , color, vist)
            dfs(grid, r, c - 1, color, vist)
            
            vist.remove((r,c))
            return image
        
        return dfs(image, sr, sc, color, set())
        