# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        listOnePointer = list1
        listTwoPointer = list2 
        dummy = ListNode()
        tail = dummy


        while listOnePointer and listTwoPointer: 
            if listOnePointer.val <= listTwoPointer.val:
                tail.next = listOnePointer
                listOnePointer = listOnePointer.next
            else: 
                tail.next = listTwoPointer
                listTwoPointer = listTwoPointer.next
            tail = tail.next

        if listOnePointer:
            tail.next = listOnePointer
        if listTwoPointer:
            tail.next = listTwoPointer

        return dummy.next


