# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            return TreeNode(val, root)
        
        def dfs(node, depth):
            if depth == 1:
                left = TreeNode(val, node.left)
                right = TreeNode(val, None, node.right)
                node.left = left
                node.right = right
            else:
                depth -= 1
                if node.left:
                    dfs(node.left, depth)
                if node.right:
                    dfs(node.right, depth)

        depth -= 1
        dfs(root, depth)
        return root
                