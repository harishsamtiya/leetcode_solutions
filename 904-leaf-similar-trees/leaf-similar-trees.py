# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1_leafs = []
        tree2_leafs = []

        def dfs(node, leaf_nodes):
            if node:
                if not node.left and not node.right:
                    leaf_nodes.append(node.val)
                    return
                dfs(node.left, leaf_nodes)
                dfs(node.right, leaf_nodes)
            return
        
        dfs(root1, tree1_leafs)
        dfs(root2, tree2_leafs)
        return tree1_leafs == tree2_leafs