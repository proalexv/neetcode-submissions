# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal could have us vist elements from least to greatest, storing them in the arrary and then finding the kth + 1 index (given arrays are 0 based and). this would be and o(n) operation for time alon with a space complexity of o(n) given we need to create an arrary to store said vlues. 
        sortedArrary = []
        def inorder(root):
            if not root: 
                return
           
            inorder(root.left)
            sortedArrary.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return sortedArrary[k - 1]