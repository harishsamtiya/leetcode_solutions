class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def digit_count(num):
            count = 0

            while num:
                num //= 10
                count += 1
            return count
        ld, hd = digit_count(low), digit_count(high)

        result = []
        for i in range(ld, hd+1):
            for j in range(1, 11-i):
                temp = 0
                for k in range(i):
                    temp = temp*10
                    temp += (j+k)

                if temp >= low:
                    if temp <= high:
                        result.append(temp)
                    else:
                        break
                
        
        return result