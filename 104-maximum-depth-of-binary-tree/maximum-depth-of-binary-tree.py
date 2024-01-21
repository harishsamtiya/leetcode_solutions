# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        height = 0

        stack = [(root, 0)]

        while stack:
            node, curr_height = stack.pop()
            if node.left:
                stack.append((node.left, curr_height +1))
            if node.right:
                stack.append((node.right, curr_height + 1))
            height = max(height, curr_height + 1)
        return height
