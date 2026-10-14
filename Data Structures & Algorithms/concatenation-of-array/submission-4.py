class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lengthOfNums = len(nums)
        ans = [0] * (2* lengthOfNums)
        for i in range(lengthOfNums):
             ans[i],ans[i + lengthOfNums] = nums[i],nums[i]
        return ans
        