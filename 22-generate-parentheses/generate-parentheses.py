class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        li = [("", 0, 0)]
        result = []
        while li:
            st, op, cl = li.pop()
            if cl == n:
                result.append(st)
            if op < n:
                li.append((st+"(", op+1, cl))
            if cl < op:
                li.append((st+")", op, cl+1))
        return result


            