class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixArray = []
        for arrary in matrix:
            total = 0
            subarrary = []
            for element in arrary:
                total += element
                subarrary.append(total)
            self.prefixArray.append(subarrary)
                 
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int)-> int:
        total = 0
        for i in range(row1, row2 + 1): 
            subarrayOfPrefix = self.prefixArray[i]
            if col1 == 0: 
                total += subarrayOfPrefix[col2]
            else:
                total +=  subarrayOfPrefix[col2] - subarrayOfPrefix[col1 - 1]
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)