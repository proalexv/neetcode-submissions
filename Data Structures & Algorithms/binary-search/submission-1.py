class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Left and right pointer starting at 0, and at the end of the arrary 
        L, R = 0, len(nums) - 1

        # Calculate the midpoints of L and R and compare the target to the mid point, if targert is greater then the midpoint, move the L pointer to mid + 1, inversely, if its smaller, move right pointer to mid - 1
        while L <=R: 
            midpoint = ( L + R ) // 2 

            # if the value is not > or <, then it is = value 
            if (target > nums[midpoint]): 
                L = midpoint + 1
            elif (target < nums[midpoint]):
                R = midpoint - 1
            else: 
                return midpoint
        return -1 

            # if no values are + targert return -1 