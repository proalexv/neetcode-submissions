import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Converting the array into a max heap:  
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            first_stone = heapq.heappop_max(stones)
            secound_stone = heapq.heappop_max(stones)
            smash_result = first_stone - secound_stone 

            if smash_result != 0: 
                heapq.heappush_max(stones, smash_result)
            
        if len(stones) == 0: 
            return 0 
        else: 
            return heapq.heappop_max(stones)