class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums): 
            for i in range(len(nums) - 1):
                if index != i + 1:
                    if num + nums[i + 1] == target:
                        return [index, i + 1] 
            