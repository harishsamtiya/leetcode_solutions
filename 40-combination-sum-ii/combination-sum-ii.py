class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        result = []

        while n >= 0 and candidates[n-1] > target:
            n -= 1


        def backtrack(ind, summ, li):
            if ind >= n or summ >target:
                if summ == target:
                    result.append(li.copy())
                return
            
            li.append(candidates[ind])
            summ += candidates[ind]
            backtrack(ind+1, summ, li)

            li.pop()
            summ -= candidates[ind]
            while ind + 1 < n and candidates[ind] == candidates[ind+1]:
                ind += 1
            
            backtrack(ind+1, summ, li)

        backtrack(0, 0, [])
        return result

            