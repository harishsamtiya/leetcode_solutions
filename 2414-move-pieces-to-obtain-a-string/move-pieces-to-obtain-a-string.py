class Solution:
    def canChange(self, start: str, target: str) -> bool:
        li = list(start)
        n = len(start)
        curr = 0

        for i in range(n):
            tch = target[i]
            curr = max(curr, i)
            if tch == 'L':
                while curr < n:
                    if li[curr] == 'L':
                        li[curr], li[i] = li[i], li[curr]
                        curr += 1
                        break
                    elif li[curr] == 'R':
                        return False
                    curr += 1
                
        curr = n-1
        for i in range(n-1, -1, -1):
            tch = target[i]
            curr = min(i, curr)
            if tch == 'R':
                while curr >= 0:
                    if li[curr] == 'L':
                        return False
                    elif li[curr] == 'R':
                        li[curr], li[i] = li[i], li[curr]
                        curr -= 1
                        break
                    curr -= 1
        

        for i in range(n):
            if target[i] != li[i]:
                return False

        return True