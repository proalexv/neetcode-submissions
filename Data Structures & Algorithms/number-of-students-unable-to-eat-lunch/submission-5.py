from collections import deque, Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # studentsDeque = deque(students)
        # sandwichesDeque = deque(sandwiches)

        # while sandwichesDeque: 
        #     currentSandwhich = sandwichesDeque.popleft()
        #     currentStudent = studentsDeque.popleft() 
        #     counter = 0
            
        #     while currentStudent != currentSandwhich:
        #         studentsDeque.append(currentStudent)
        #         currentStudent = studentsDeque.popleft()
        #         counter += 1
        #         if counter > len(sandwichesDeque):
        #             return len(sandwichesDeque)
            
        #     sandwichesDeque.popleft()
        #     studentsDeque.popleft()
        
        # return len(sandwichesDeque)
        studentsCounter = Counter(students)
        sandwichesDeque = deque(sandwiches)

        while sandwichesDeque:  
            if studentsCounter[sandwichesDeque[0]] > 0:
                studentsCounter[sandwichesDeque[0]] -=1
                sandwichesDeque.popleft()     
            else: 
                break
        return len(sandwichesDeque)
            

            
