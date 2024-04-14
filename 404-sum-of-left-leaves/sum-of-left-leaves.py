# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.result = 0

        def dfs(node, isleft):
            if node.left or node.right:
                if node.left:
                    dfs(node.left, True)
                if node.right:
                    dfs(node.right, False)
            else:
                if isleft:
                    self.result += node.val
        
        dfs(root, False)
        return self.result