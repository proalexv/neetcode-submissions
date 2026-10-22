# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # size = 0 
        # current = head
        # while current: 
        #     current = current.next
        #     size += 1
        
        # firstPointer = head
        # secoundPointer = head
        # maxVal = -1
        # for _ in range((size//2)):
        #     secoundPointer = secoundPointer.next

        # while secoundPointer: 
        #      maxVal = max(maxVal, firstPointer.val + secoundPointer.val)
        #      firstPointer = firstPointer.next
        #      secoundPointer = secoundPointer.next
       
        # return maxVal

        slow = head 
        fast = head
        prev = None
        while fast and fast.next: 
            fast = fast.next.next 
            current = slow.next
            slow.next = prev
            prev = slow
            slow = current 
        maxValue = -1
        while slow:
            maxValue = max(maxValue, slow.val + prev.val)  
            slow,prev = slow.next, prev.next
        return maxValue


