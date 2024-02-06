# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        n = len(preorder)
        self.pind = 0
        def fun(start, end):
            if start > end:
                return None
            
            node = TreeNode(preorder[self.pind])
            ind = 0
            for i in range(start, end+1):
                if inorder[i] == preorder[self.pind]:
                    ind = i
                    break
            
            self.pind += 1
            node.left = fun(start, ind-1)
            node.right = fun(ind+1, end)
            return node
        return fun(0, n-1)
