class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers=[1,2,3,4]
        L,R = 0, (len(numbers) - 1)
        
        while L < R:
            if numbers[L] + numbers[R] == target: 
                return [L + 1, R + 1]
            else: 
                if numbers[L] + numbers[R] > target:
                    R -= 1
                else: 
                    L += 1
        