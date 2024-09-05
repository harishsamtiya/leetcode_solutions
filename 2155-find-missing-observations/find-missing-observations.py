class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_summ = mean*(n+m)
        observed_sum = sum(rolls)

        remain_sum = total_summ - observed_sum

        if remain_sum < n or remain_sum > 6*n:
            return []
        
        result = []
        me = remain_sum//n
        for _ in range(n):
            result.append(me)

        mod = remain_sum%n
        for i in range(mod):
            result[i] += 1
        return result