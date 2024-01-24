# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        queue = [None, root]
        result = []

        while True:
            node = queue.pop(0)
            if node:
                result[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                if not queue:
                    break
                else:
                    result.append(list())
                    queue.append(None)

        return result