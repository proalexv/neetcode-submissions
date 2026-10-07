class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNumOfOnes = 0
        currentCountOfOnes= 0 

        for num in nums: 
            if num == 1: 
                currentCountOfOnes +=1 
                maxNumOfOnes = max(maxNumOfOnes,currentCountOfOnes )
            else: 
                currentCountOfOnes = 0; 
        return maxNumOfOnes

       
