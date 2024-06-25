# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def dfs(node, parentRightNodeSumm):
            if node:
                temp = node.val
                rightSumm = dfs(node.right, parentRightNodeSumm)
                leftSumm = dfs(node.left, rightSumm + parentRightNodeSumm + temp)
                node.val += rightSumm + parentRightNodeSumm
                return temp + rightSumm + leftSumm
            return 0
        dfs(root, 0)
        return root