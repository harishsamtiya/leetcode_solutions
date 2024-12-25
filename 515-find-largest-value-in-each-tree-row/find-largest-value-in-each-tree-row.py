# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [(0, root)]

        result = []
        n = 0

        while stack: 
            level, node = stack.pop()

            if level < n:
                result[level] = max(result[level], node.val)
            else:
                result.append(node.val)
                n += 1

            if node.right:
                stack.append((level+1, node.right))
            
            if node.left:
                stack.append((level+1, node.left))
        
        return result