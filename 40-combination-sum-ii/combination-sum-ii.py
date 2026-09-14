class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        my_ans = []

        candidates_dict = dict()
        for candidate in candidates:
            if candidate in candidates_dict:
                candidates_dict[candidate] += 1
            else:
                candidates_dict[candidate] = 1
        
        candidates = [(val, cnt) for val, cnt in candidates_dict.items()]
        n = len(candidates)
        candidates.sort(key=lambda x: x[0])
        def solve(i, arr, summ):
            if target == summ:
                my_ans.append(arr)
            if i < n and summ < target:
                
                val, cnt = candidates[i]
                solve(i+1, arr, summ)

                for c in range(1, cnt+1):
                    solve(i+1, arr + [val]*c, summ+(val*c))
        
        solve(0, [], 0)
        return my_ans
                        

