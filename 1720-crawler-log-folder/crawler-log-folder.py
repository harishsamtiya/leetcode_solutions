class Solution:
    def minOperations(self, logs: List[str]) -> int:
        minop = 0

        for dir in logs:
            if dir == '../':
                minop = max(minop-1, 0)
            elif dir == './':
                minop += 0
            else: 
                minop += 1
        
        return abs(minop)