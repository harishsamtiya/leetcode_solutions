class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []

        for ch in s:
            asciCurr = ord(ch)
            if stack:
                asciiPrev = ord(stack[-1])
                if asciiPrev -32 == asciCurr or asciiPrev + 32 == asciCurr:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        

        return "".join(stack)
