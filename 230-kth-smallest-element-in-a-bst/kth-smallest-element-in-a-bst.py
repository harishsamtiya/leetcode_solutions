# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.p = 0
        def preOrder(node):
            if node:
                left = preOrder(node.left)
                if left != -1:
                    return left
                self.p += 1
                if self.p == k:
                    return node.val
                
                return preOrder(node.right)
            return -1
        return preOrder(root)
                