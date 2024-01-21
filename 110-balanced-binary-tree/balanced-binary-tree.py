# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balanced(node):
            if node:
                l_height, l_balanced = balanced(node.left)
                if not l_balanced:
                    return (0, False)
                
                (r_height, r_balanced) = balanced(node.right)
                if not r_balanced:
                    return (0, False)

                if -1 <= r_height - l_height <= 1:
                    return (max(l_height, r_height) +1, True)
                else:
                    return (0, False)
            
            return (0, True)
        return balanced(root)[1]