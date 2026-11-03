# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # Base case
        if not root: 
            return None 
        
        # Traverse down the tree untill key is found
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val: 
            root.left = self.deleteNode(root.left, key)
        # We have found the element
        else:
            if not root.left: 
                return root.right 
            elif not root.right:
                return root.left
            else: 
                # Node has 2 childern 
                curr = root.right 
                while curr and curr.left: 
                    curr = curr.left 
                
                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)

        return root