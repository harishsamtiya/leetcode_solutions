class Solution:
    def minOperations(self, s: str) -> int:

        def fun(prev):
            count = 0
            for ch in s:
                if ch == '0':
                    if not prev:
                        count += 1
                        prev = True
                    else:
                        prev = False
                elif ch == '1':
                    if prev:
                        count += 1
                        prev = False
                    else:
                        prev = True
            return count
        
        return min(fun(False), fun(True))