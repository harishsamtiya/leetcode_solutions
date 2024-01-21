# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        result = 0
        def maxdia(node):
            nonlocal result
            if node:
                left = maxdia(node.left)
                right = maxdia(node.right)
                result = max(result, left+right+1)
                return max(left, right) + 1 
            return 0
        maxdia(root)
        return result-1