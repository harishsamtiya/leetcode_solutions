class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        result = []

        def find_next_ind(ind):
            if ind >= n-1:
                return float('inf')
            next_ind = ind
            for i in range(ind+1, n):
                if candidates[i] == candidates[ind]:
                    next_ind = i
                else:
                    break
            next_ind += 1
            if next_ind >= n:
                return float('inf')
            return next_ind

        def solve(li, ind, summ):
            if summ <= target:
                if ind == n:
                    if summ == target:
                        result.append(li.copy())
                else:
                    next_ind = find_next_ind(ind)
                    solve(li, min(next_ind, n), summ)
                    
                    for i in range(ind, min(next_ind, n)):
                        summ += candidates[i]
                        li.append(candidates[i])
                        solve(li, min(next_ind, n), summ)
                    
                    for i in range(ind, min(next_ind, n)):
                        summ -= candidates[i]
                        li.pop()

        solve([], 0, 0)
        return result