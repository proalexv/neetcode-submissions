# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def postorder(root):
            if not root:
                return [True, 0]

            LEFT = postorder(root.left)
            RIGHT = postorder(root.right)

            balanced = LEFT[0] and RIGHT[0] and abs(LEFT[1] - RIGHT[1]) <= 1
            return [balanced, 1 + max(LEFT[1], RIGHT[1])]

        return postorder(root)[0]