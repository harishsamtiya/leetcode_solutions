# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        result = 0
        curr = [root]
        val_to_inds = [-1]*100001

        while curr:
            n = len(curr)
            temp = []
            vals = []
            for i in range(n):
                node = curr[i]
                if node.left:
                    temp.append(node.left)
                
                if node.right:
                    temp.append(node.right)
                vals.append(node.val)
                val_to_inds[node.val] = i
            
            vals.sort()
            count = 0
            for i in range(n-1):
                minInd = val_to_inds[vals[i]]
                if minInd != i:
                    count += 1
                    val_to_inds[curr[i].val], val_to_inds[curr[minInd].val] = minInd, i
                    curr[i].val, curr[minInd].val = curr[minInd].val, curr[i].val

            result += count
            curr = temp

        return result
            