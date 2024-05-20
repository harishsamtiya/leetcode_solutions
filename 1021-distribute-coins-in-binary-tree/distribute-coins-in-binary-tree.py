# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node):
            if node:
                coins = node.val 

                left = dfs(node.left)
                right = dfs(node.right)

                if left >= 0:
                    self.moves += left
                    coins += left
                    left = 0
                else:
                    left = -left
                
                if right >= 0:
                    coins += right
                    self.moves += right
                    right = 0
                else:
                    right = -right
                
                remain = left + right + 1
                self.moves += remain - 1

                return coins - remain
            return 0

        dfs(root)
        return self.moves
                