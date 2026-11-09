# import copy 
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         answerArr= [[]]
#         for num,Arr  in nums, deep_copied_arr: 
#                 deep_copied_arr = copy.deepcopy(Arr)
#                 for array in deep_copied_arr: 
#                     deep_copied_arr.append(array.append(num))

            
                 
#         return answerArr

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for i in range(len(res)):      # range is evaluated once, so it's a fixed snapshot
                res.append(res[i] + [num])  # + creates a new list, so it's a copy
        return res