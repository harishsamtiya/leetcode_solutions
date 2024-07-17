# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        roots = []
        
        myset = set(to_delete)

        def dfs(node):
            if node:

                left = dfs(node.left)
                right = dfs(node.right)

                if left:
                    node.left = None
                
                if right:
                    node.right = None
                
                if node.val in myset:
                    if node.left:
                        roots.append(node.left)
                    if node.right:
                        roots.append(node.right)
                    return True
                
            return False
        
        flag = dfs(root)
        if not flag:
            roots.append(root)
        return roots
