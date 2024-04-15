# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        stack = [(root, 0)]
        result = 0
        mod = 2**32
        while stack:
            node, summ = stack.pop()
            summ = summ*10 + node.val
            if node.left or node.right:
                if node.right:
                    stack.append((node.right, summ))
                if node.left:
                    stack.append((node.left, summ))
            else:
                result += summ
                result %= mod
                
        return result