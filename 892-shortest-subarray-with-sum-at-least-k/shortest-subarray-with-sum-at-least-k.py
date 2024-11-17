class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        curr_summ = 0
        q = deque()
        result = n + 1 

        for i in range(n):
            curr_summ += nums[i]

            if curr_summ >= k:
                result = min(i+1, result)
            
            while q and curr_summ - q[0][0] >= k:
                prev_summ, ind = q.popleft()
                result = min(result, i - ind)

            while q and q[-1][0] > curr_summ:
                q.pop()
            q.append((curr_summ, i))


        if result == n+1:
            return -1
        return result