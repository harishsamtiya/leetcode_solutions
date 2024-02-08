class Solution:
    def numSquares(self, n: int) -> int:
        
        array = [p*p for p in range(1,int(n**(0.5)) + 1)]
        print(array)
        result = [-1]*(n+1)
        result[0] = 0

        for num in range(1, n+1):
            temp = num
 
            for sq in array:
                if sq > num:
                    break

                temp = min(temp, result[num-sq] + 1)

            result[num] = temp

        return result[n]
            

