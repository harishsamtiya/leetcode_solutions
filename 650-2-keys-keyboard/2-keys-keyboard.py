class Solution:
    def minSteps(self, n: int) -> int:
        
        def highestFactors(num):
            for q in range(num//2, 1, -1):
                if num%q == 0:
                    return q, num//q
            return num, 1
        
        array = [0]*(n+1)
        
        for num in range(2, n+1):
            q1, q2 = highestFactors(num)
            
            if q1 == num:
                array[num] = num
            else:
                array[num] = array[q1] + q2

        return array[-1]
