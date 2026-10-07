class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Trivial solution with 2 loops so O(n^2) time and space complexity of O(1)
        # maxSum = nums[0]
        # for i in range(len(nums)):
        #     curSum = 0
        #     for j in range(i , len(nums)): 
        #         curSum += nums[j]
        #         maxSum = max(maxSum, curSum)
        # return maxSum

        #2 pointer solution or kadanes algo with o(n) time space complexity and o(1) time complextiy

        maxSum, curSum = nums[0], 0
        maxL,maxR,L,R = 0,0,0,0

        for R in range(len(nums)):
            if curSum < 0: 
                curSum =0
                L = R 
            curSum += nums[R]
            
            if curSum > maxSum: 
                maxSum = curSum 
                maxL,maxR = L,R 
        return maxSum





        

