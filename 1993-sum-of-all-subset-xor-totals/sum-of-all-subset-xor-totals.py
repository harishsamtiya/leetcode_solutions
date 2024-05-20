class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        stack = [(0, 0)]
        result = 0

        while stack:
            ind, xor = stack.pop()

            if ind == n:
                result += xor
            else:
                stack.append((ind+1, xor))
                xor ^= nums[ind]
                stack.append((ind+1, xor))
        return result