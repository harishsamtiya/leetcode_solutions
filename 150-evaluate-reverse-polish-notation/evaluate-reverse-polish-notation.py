class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()

                if token == '/' :
                    if num2 == 0:
                        stack.append(0)
                    else:
                        stack.append(int(num1/num2))
                else:
                    stack.append(eval(str(num1)+token+str(num2)))
            else:
                stack.append(eval(token))

        return stack[-1]