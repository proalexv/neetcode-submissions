from heapq import heapify, heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap_nums = nums
        self.k = k
    
    def add(self, val: int) -> int:
        heapq.heappush(self.heap_nums, val)
        number_of_pops = len(self.heap_nums) - self.k
        while number_of_pops > 0:
            kthLargest = heapq.heappop(self.heap_nums)
            number_of_pops -= 1
        return self.heap_nums[0]
