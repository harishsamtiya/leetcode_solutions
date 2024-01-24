# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, lb, ub):
            if node:
                if lb<= node.val <= ub:
                    return  isValid(node.left, lb, node.val-1) and isValid(node.right, node.val + 1, ub)
                else:
                    return False
            return True
        ub = 2**31
        return isValid(root, -1*ub, ub -1)