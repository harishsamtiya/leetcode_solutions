class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minqueue = deque()
        maxqueue = deque()

        n = len(nums)

        start = 0
        result = 1

        for i in range(n):

            while minqueue and nums[minqueue[-1]] >= nums[i]:
                minqueue.pop()
            minqueue.append(i)

            
            while maxqueue and  nums[maxqueue[-1]] <= nums[i]:
                maxqueue.pop()
            maxqueue.append(i)

            while True :
                minInd = minqueue[0]
                maxInd = maxqueue[0]
                limitCheck = nums[maxInd] - nums[minInd]
                if limitCheck <= limit:
                    break
                ind = min(minInd, maxInd)
                start = ind + 1
                if minqueue[0] <= ind:
                    minqueue.popleft()
                if maxqueue[0] <= ind:
                    maxqueue.popleft()
            
            result = max(result, i-start+1)
        return result
                
            