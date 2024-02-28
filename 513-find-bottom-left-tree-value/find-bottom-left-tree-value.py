# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.height = 0
        self.value = root.val

        def dfs(node, heigh):
            if node:
                dfs(node.left, heigh+1)
                dfs(node.right, heigh+1)
                if (not (node.left or node.right)) and heigh > self.height:
                    self.height = heigh
                    self.value = node.val
        dfs(root, 0)
        return self.value