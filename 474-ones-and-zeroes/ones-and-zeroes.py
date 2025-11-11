class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        li = []
        self.lenStrs = len(strs)
    
        for st in strs:
            zeroCnt = 0
            for ch in st:
                if ch == '0':
                    zeroCnt += 1
            li.append((zeroCnt, len(st) - zeroCnt))
        dp = dict()
        def solve(i, m, n):
            if (m <= 0 and n <= 0) or i >= self.lenStrs:
                return 0
            elif (i, m, n) in dp:
                return dp[(i, m, n)]
            zeroCnt, oneCnt = li[i]
            ans = solve(i+1, m, n)
            if m >= zeroCnt and n >= oneCnt:
                ans = max(ans, solve(i+1, m -zeroCnt, n-oneCnt) + 1)
            dp[(i, m, n)] = ans
            return ans
        
        return solve(0, m, n)
            
