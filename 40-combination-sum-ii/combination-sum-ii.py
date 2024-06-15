class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        candidates.sort()

        combinations = []
        
        def backtrack(i, li, summ):
            if summ == target:
                combinations.append(li.copy())
                return
            elif i >= n or summ > target:
                return

            li.append(candidates[i])
            summ += candidates[i]
            backtrack(i+1, li, summ)

            li.pop()
            summ -= candidates[i]

            while i + 1 < n and candidates[i+1] == candidates[i]:
                i += 1

            backtrack(i+1, li, summ)
        
        backtrack(0, [], 0)
        return combinations