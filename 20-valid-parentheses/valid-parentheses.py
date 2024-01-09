class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == ')' :
                if not stack or '(' != stack.pop():
                    return False
            elif ch == '}' :
                if not stack or '{' != stack.pop():
                    return False 
            elif ch == ']' :
                if not stack or '[' != stack.pop():
                    return False
            else:
                stack.append(ch)
            
        if stack:
            return False
        return True