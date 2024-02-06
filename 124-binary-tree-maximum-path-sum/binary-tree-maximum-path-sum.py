# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        def dfs(node):
            if node:
                left = max(0, dfs(node.left))
                right = max(0, dfs(node.right))
                self.ans = max(self.ans, node.val + left + right)
                return node.val + max(left, right)
                
            return 0
        dfs(root)
        return self.ans