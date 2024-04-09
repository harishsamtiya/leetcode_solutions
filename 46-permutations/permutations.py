class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def backtrack(array):
            if len(array) == n:
                result.append(array.copy())
            else:
                for i in range(n):
                    if nums[i] < 11:
                        array.append(nums[i])
                        nums[i] += 30
                        backtrack(array)
                        nums[i] -= 30
                        array.pop()

        backtrack([])
        return result
