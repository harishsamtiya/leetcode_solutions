class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n

        stack = []
        for i in range(n):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                ind = stack.pop()
                result[ind] = i-ind
            
            stack.append(i)
        
        while stack:
            ind = stack.pop()
            result[ind] = 0
        return result

