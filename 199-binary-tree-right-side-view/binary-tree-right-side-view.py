# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        result = []
        queue = [root, None]

        while True:
            node = queue.pop(0)
            result.append(node.val)

            while node:
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

                node = queue.pop(0)
            if queue:
                queue.append(node)
            else:
                break
            
        return result