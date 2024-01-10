class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n

        stack = [(0, temperatures[0])]
        for i in range(1, n):
            temp = temperatures[i]
            ind, top = stack[-1]
            while temp > top:
                stack.pop()
                result[ind] = i - ind
                if stack:
                    ind, top = stack[-1]
                else:
                    break
            stack.append((i, temp))

        
        return result
                