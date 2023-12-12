class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        ans = keysPressed[0]
        maxi = releaseTimes[0]
        for i in range(1, n):
            curr = releaseTimes[i]- releaseTimes[i-1]
            if curr > maxi:
                ans = keysPressed[i]
                maxi = curr
            elif curr == maxi and ans < keysPressed[i]:
                ans = keysPressed[i]


        return ans