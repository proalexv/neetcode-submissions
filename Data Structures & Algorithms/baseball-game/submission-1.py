class Solution:
    def calPoints(self, operations: List[str]) -> int:
        answerArr = []
        for operation in operations: 
            if operation == "+":
                answerArr.append(answerArr[-1] + answerArr[-2])
            elif operation == "D":
                answerArr.append(answerArr[-1]*2)
            elif operation == "C":
                answerArr.pop()
            else: 
                answerArr.append(int(operation))
        return sum(answerArr)
                

