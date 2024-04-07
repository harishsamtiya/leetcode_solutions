class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        result = []

        def backtrack(ind, array, summ):
            if n == ind:
                if summ == target:
                    result.append(array.copy())
            else:
                if summ == 0 or array[-1] != candidates[ind]:
                    backtrack(ind+1, array, summ)
                array.append(candidates[ind])
                summ += candidates[ind]

                if summ == target:
                    result.append(array.copy())
                elif summ < target:
                    backtrack(ind, array, summ)
                    backtrack(ind+1, array, summ)
                print(array, summ, ind)
                array.pop()
                summ -= candidates[ind]
            
        backtrack(0, [], 0)
        return result