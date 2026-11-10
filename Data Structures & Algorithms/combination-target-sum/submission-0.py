class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        path, sol = [], []
        
        def dfs (index, total):
            # Base Cases 
            if (index >= len(nums)) or (total > target):
                return 
            
            if total == target:
                sol.append(path[:])
                return

            
            # We don't inculde the number
            dfs(index + 1, total)

            # We inculde the number
            path.append(nums[index])
            dfs(index, total + nums[index])

            #Backtracking to undue our addition
            path.pop()
    

        dfs(0,0)
        return sol
            
        