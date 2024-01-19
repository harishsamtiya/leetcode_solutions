class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        ind = 0
        stack = []
        for i in range(k):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])
        
        result = [stack[0]]
        l = 0
        for i in range(k, n):
            if stack[0] == nums[l]:
                stack.pop(0)

            while stack and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])

            l += 1
            result.append(stack[0])
        return result