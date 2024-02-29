# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        queue = [root, None]
        isEven = True
        maxi = 0
        maxmini = 10**6 + 1
        mini = maxmini

        while queue:
            node = queue.pop(0)

            if not node:
                if queue:
                    isEven = not isEven
                    queue.append(None)
                    maxi = 0
                    mini = maxmini
                    continue
                else:
                    return True

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

            if isEven:
                if node.val%2==1 and maxi < node.val:
                    maxi = node.val
                else:
                    return False
            else:
                if node.val%2==0 and node.val < mini:
                    mini = node.val
                else:
                    return False
