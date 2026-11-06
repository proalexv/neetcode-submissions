# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue =  deque()
        array = []
        if root: 
                queue.append(root)
        
        while len(queue):
            size = len(queue)
            for i in range(len(queue)):
                curr = queue.popleft()
                if i == (size - 1):
                    array.append(curr.val)
                if curr.left: 
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
            
        return array
             