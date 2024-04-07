class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def backtrack(ind, listSet):
            if ind == n:
                result.append(listSet.copy())
            else:
                backtrack(ind+1, listSet)
                listSet.append(nums[ind])
                backtrack(ind+1, listSet)
                listSet.pop()
        
        backtrack(0, [])
        return result