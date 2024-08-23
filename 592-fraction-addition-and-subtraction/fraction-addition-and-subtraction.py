class Solution:
    def fractionAddition(self, expression: str) -> str:
        n = len(expression)
        denos = [0]*11

        symbol = "+"

        for i in range(n):
            ch = expression[i]
            if ch == "+" or ch == "-":
                symbol = ch
            elif ch == "/":
                nume = int(expression[i-1])
                if nume == 0 :
                    nume = 10
                if symbol == '-':
                    nume *= -1
                deno = int(expression[i+1])
                if deno == 1 and i+2 < n and expression[i+2] == '0':
                    deno = 10
                denos[deno] += nume
            

        deno = 1
        nume = 0
        for i in range(1, 11):
            if denos[i] != 0:
                deno *= i
        
        for i in range(1, 11):
            nume += denos[i]*(deno//i)
        
        for i in range(11, 1, -1):
            if nume%i == 0 and deno%i ==0:
                nume //= i
                deno //= i
        
        return f'{nume}/{deno}'