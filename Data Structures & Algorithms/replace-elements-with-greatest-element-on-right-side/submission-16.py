class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # # Brute Force: 
        answer = []
        for i in range(len(arr)):
            if i == len(arr) - 1: 
                answer.append(-1)
            else: 
                maxValue = max(arr[i+1:])
                answer.append(maxValue)
        return answer 


