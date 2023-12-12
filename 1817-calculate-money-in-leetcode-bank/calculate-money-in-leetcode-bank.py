class Solution:
    def totalMoney(self, n: int) -> int:
        wn = n//7
        sn = int(wn*(56 + 7*(wn - 1))/2)
        n = n - 7*wn

        sn += sum(range(1, n+1)) + n*wn
        return sn
