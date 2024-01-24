# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        # if q.val < p.val:
        #     p, q = q, p

        def dfs(node, lb, ub):
            if not node:
                return 0

            val = node.val
            left = right = 0
            if lb <= p.val <= val - 1 or lb <= q.val <= val - 1:
                left = dfs(node.left, lb, val-1)
            
            if left == 3:
                return 3
            
            if val + 1 <= q.val <= ub or val + 1 <= p.val <= ub:
                right = dfs(node.right, val+1, ub)

            if right == 3:
                return 3
            
            center = 0
            if (val == p.val or val == q.val):
                center = 1
            # print(val, left, right, center)
            if left + right + center == 2:
                self.ans = node
                return 3
            else:
                return left + right + center
        
        ub = 10**9
        dfs(root, -1*ub, ub)
        return self.ans
