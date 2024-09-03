class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = dict()

        def solve(ind):
            if ind == n:
                return  True
            elif ind in memo:
                return memo[ind]
            else:

                for st in  wordDict:
                    m = len(st)
                    if n - ind < m:
                        continue
                    
                    if s[ind: ind + m] == st:
                        if solve(ind + m):
                            memo[ind] = True
                            return True
                
                memo[ind] = False
                return False
        
        return solve(0)