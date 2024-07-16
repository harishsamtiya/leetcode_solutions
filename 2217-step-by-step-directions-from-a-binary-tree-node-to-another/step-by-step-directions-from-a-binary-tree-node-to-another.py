# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.start = ""
        self.dest = ""

        def dfs(node):
            if node:
                temp = 0
                if node.val == startValue:
                    temp = 1
                elif node.val == destValue:
                    temp = 2
                
                
                left = dfs(node.left)
 
                right = dfs(node.right)

                
                if left == 1 or right == 1:
                    self.start = self.start + "U"
                    temp += 1

                
                if left == 2:
                    self.dest = "L" + self.dest
                    temp += 2
                elif right == 2:
                    self.dest = "R" + self.dest
                    temp += 2
                
                return temp
            
        dfs(root)
        return self.start + self.dest