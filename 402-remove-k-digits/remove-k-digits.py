class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n <= k:
            return '0'
        stack = []

        i = 0

        while k > 0 and i < n:
            if not stack:
                if num[i] != '0':
                    stack.append(num[i])
                i += 1
            elif num[i] >= stack[-1]:
                stack.append(num[i])
                i += 1
            elif stack[-1] > num[i]:
                stack.pop()
                k -= 1
            

        
        while stack and k > 0:
            stack.pop()
            k -= 1

        while not stack and i < n and num[i] == '0':
            i += 1

        result = "".join(stack) + num[i:]
        return "0" if result == "" else result
