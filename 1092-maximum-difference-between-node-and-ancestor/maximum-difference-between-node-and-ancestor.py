# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, maxi, mini):
            if node:
                ans = max(abs(node.val - maxi), abs(node.val - mini))
                maxi = max(node.val, maxi)
                mini = min(node.val, mini)
                
                
                return max(ans, max(dfs(node.left, maxi, mini), dfs(node.right, maxi, mini)))
            return 0
        
        return dfs(root, root.val, root.val)