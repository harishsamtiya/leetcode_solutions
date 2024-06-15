class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        powerSet = []

        def backtrack(i, li):
            if i == n:
                powerSet.append(li.copy())
            else:
                li.append(nums[i])
                backtrack(i+1, li)
                li.pop()

                while i + 1 < n and nums[i] == nums[i+1]:
                    i += 1
                backtrack(i+1, li)
        
        backtrack(0, [])
        return powerSet