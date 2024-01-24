# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        array = [0]*10

        def ispalindromic(array, h):
            if h%2 :
                notOne = True
                for num in array:
                    if num%2:
                        if notOne:
                            notOne = False
                        else:
                            return False
                return True
            else:
                for num in array:
                    if num%2:
                        return False
                return True
                    

        def backtrack(node, h):
            array[node.val] += 1
            ans = 0
            
            if not (node.left or node.right):
                if ispalindromic(array, h):
                    ans = 1
                array[node.val] -= 1
                return ans

            if node.left:
                ans += backtrack(node.left, h+1)
            
            if node.right:
                ans += backtrack(node.right, h+1)
            array[node.val] -= 1
            return ans
        
        return backtrack(root, 1)
