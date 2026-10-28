class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute Force
        # eatSpeed = 1
        # counter = 0
        # copyPiles = piles.copy()
        # while True: 
        #     for i in range(len(piles)):
        #         while piles[i] > 0: 
        #             piles[i] -= eatSpeed 
        #             counter += 1
        #     if counter <= h:
        #         return eatSpeed
        #     else: 
        #         eatSpeed +=1
        #         counter = 0
        #         piles = copyPiles.copy()

        L,R  = 1, max(piles) 
        answer = 0 
        while L <= R: 
            M = (L + R) // 2
            count = isCorrect(M,piles)
            if count > h:
                L = M + 1 
            elif count <= h:
                R = M - 1
                answer = M 
        return answer



def isCorrect(M, piles):
    count = 0 
    for i in range(len(piles)):
        count += math.ceil(piles[i] / M)
    return count
 

            
            
        

