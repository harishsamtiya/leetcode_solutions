class Solution:
    def pivotInteger(self, n: int) -> int:
        
        x = ((n*n + n)/2)**(0.5)
        
        if x == int(x):
            return int(x)

        return -1