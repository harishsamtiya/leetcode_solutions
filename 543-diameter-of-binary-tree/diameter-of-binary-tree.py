# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def depth(node):
            if  node:
                left = depth(node.left)
                right = depth(node.right)
                self.result = max(self.result, left + right + 1)
                return max(left, right) + 1
            return 0
        depth(root)
        return self.result -1
