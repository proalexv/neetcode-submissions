class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # # Brute Force: time, o(n^2), space O(n)
        # answer = []
        # for i in range(len(arr)):
        #     if i == len(arr) - 1: 
        #         answer.append(-1)
        #     else: 
        #         maxValue = max(arr[i+1:])
        #         answer.append(maxValue)
        # return answer 
        
        # Optimal solution going backwards 
        answer = []
        maxValue = -1
        for i in range(len(arr) -1, -1, -1):
            if i == len(arr) -1: 
                answer.append(-1)
                maxValue = arr[i]
            else: 
                maxValue = max(arr[i + 1], maxValue)
                answer.append(maxValue)
        return answer[::-1]



