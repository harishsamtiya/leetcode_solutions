# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        stack = [("", root)]
        result = '~'
        while stack:
            st, node = stack.pop()

            st = chr(node.val+97)+st
            if node.left or node.right:
                if node.left:
                    stack.append((st, node.left))
                
                if node.right:
                    stack.append((st, node.right))
            else:

                if st < result:
                    result = st
        return result

