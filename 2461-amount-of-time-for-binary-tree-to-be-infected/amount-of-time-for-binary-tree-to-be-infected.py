# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ans = -1
        def dfs(node):
            nonlocal ans
            if node:
                if node.val == start:
                    ans = max(dfs(node.left)[1], dfs(node.right)[1])
                    return (True, 0)
                else:
                    l_infected, l_len = dfs(node.left)
                    r_infected, r_len = dfs(node.right)

                    if l_infected or r_infected:
                        ans = max(ans, l_len + r_len + 1)
                        if l_infected:
                            return (True, l_len + 1)
                        return (True, r_len + 1)
                    else:
                        return (False, max(l_len, r_len)+1)
            return (False, 0)
        dfs(root)
        return ans