# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, maxi):
            if node:
                if maxi <= node.val:
                    self.ans += 1
                    maxi = node.val
                dfs(node.left, maxi)
                dfs(node.right, maxi)
        dfs(root, -10**4)
        return self.ans