class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # unique = sorted(set(nums))
        # nums[:len(unique)] = unique 
        # return len(unique)

        # Two pointer solution
        # [1,2,3,4,3,4]
        #        L   
        #              R     

        L, R = 1, 1

        while R < len(nums): 
            if nums[R-1] != nums[R]:
                nums[L] = nums[R]
                L +=1
                R +=1
            else: 
                 R +=1
        return L 



    

    

        
        
        
        # Bottom is wrong since it dosent consider the shifitng of the arrary
        # uniqueElements = {1}
        # for i in range(len(nums)):
        #     if nums[i] in uniqueElements: 
        #         uniqueElements.remove(nums[i])
        #     else:
        #         nums.pop(i)
        # return nums

      




        #Brute Force solution: 
    #         Create a set (no duplicates allowed) of all elements in nums, this is the answer we want but we need to modify the original arrary in place. 

    #         we loop through the original arrary element by element, if an element is in our set we keep that element in nums and pop it out of our set.
    # if an elemient is not in our set, then it has already been poped out and indicates that the element is a duplicate and must be remove from our arrary. 

    # do that untill the end of the array and we should have a non duplicated array that was modifed in place with a time complexity of o(n) and a space complexity o(n) since we created 1 set with length up to n.

   
