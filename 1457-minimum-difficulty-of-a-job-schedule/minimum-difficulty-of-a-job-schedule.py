class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if n < d:
            return -1

        cache = dict()
        def job_diff(i, d):
            if (i,d) in cache:
                return cache[(i, d)]
            if d == 1:
                return max(jobDifficulty[i:])
            today_diff = float('-inf')
            diff = float('inf')
            for j in range(i, n-d+1):
                today_diff = max(today_diff, jobDifficulty[j])
                diff = min(today_diff + job_diff(j+1, d-1), diff)
            cache[(i, d)] = diff
            return diff

        return job_diff(0, d)