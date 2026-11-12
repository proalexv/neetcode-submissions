import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # implement via heapify
        heapq.heapify_max(nums)

        while k > 1:
            heapq.heappop_max(nums)
            k -= 1
        
        return heapq.heappop_max(nums)
        
        time: O(n + Klogn)
        space: o(1)
        
        # Implement via quick select 

        # def quickSelect(left, right):
        #     pivot = nums[right]
        #     pivot_pointer = left
 
        #     for i in range(len(nums)):
        #         if nums[i] < pivot: 
        #             nums[pivot_pointer] = nums[i]
        #             pivot_pointer += 1
        #         else: 
        #             nums[i], nums[pivot_pointer] = nums[pivot_pointer], nums[i]
        #             pivot_pointer += 1

        #     if pivot == k: 
        #         return nums[pivot]
        #     elif pivot > k:

