# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same_tree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if (not root and subRoot) or (not subRoot and root):
            return False
        if (root.val != subRoot.val):
            return False
        return self.same_tree(root.left, subRoot.left) and self.same_tree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        temp = False
        if (root.val == subRoot.val):
            temp = self.same_tree(root, subRoot)
        if temp or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        return False
        