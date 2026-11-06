# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        answer = []
        if root: 
            queue.append(root)

        subarray = []

        while len(queue) > 0: 
            for i in range(len(queue)):
                curr = queue.popleft()
                subarray.append(curr.val)
                if curr.left: 
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
            
            answer.append(subarray)
            subarray = []
            
        return answer
