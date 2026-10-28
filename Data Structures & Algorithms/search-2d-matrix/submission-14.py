# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # loop through our matrix and create one big arrary 

        #assuming we appending from start of finish, we would have one big sorted arrary which we could then apply binary search too find the targert 

        # draw bag of this is the space of create a big arrary and addtional time space complexity where we may be able to optimze

        # for each arrary, run binnary search looping throught the entire 2d matrix unill the element is found or we return -1: 
        # THIS IS TOO INEEFIENT 
        # for i in range(len(matrix)):
        #     L, R = 0, (len(matrix[i]) - 1)
        #     while L <= R:  
        #         M = (L + R) // 2  
        #         if target > matrix[i][M]:
        #             L = M + 1
        #         elif target < matrix[i][M]:
        #             R = M - 1
        #         else: 
        #             return True
        # return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1 
        for i in range(len(matrix)):
            midpoint = (top + bottom) // 2
            if (matrix[midpoint][0] <= target) and (matrix[midpoint][-1] >= target):
                # regular binnary search within that arrary 
                L, R = 0, (len(matrix[midpoint]) - 1)
                while L <= R:
                    M = (L + R) //2
                    if matrix[midpoint][M] > target:
                        R = M -1
                    elif matrix[midpoint][M] < target:
                        L = M + 1
                    else: 
                        return True 
            elif matrix[midpoint][0] >= target:
                bottom = midpoint - 1
            elif matrix[midpoint][-1] <= target:
                top = midpoint + 1
        return False


    





