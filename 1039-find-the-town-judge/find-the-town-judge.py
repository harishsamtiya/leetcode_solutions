class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        array = [True]*(n)
        for a, b in trust:
            array[a-1] = False
        
        judge = -1
        for i in range(n):
            if array[i]:
                if judge == -1:
                    judge = i+1
                else:
                    return -1
        array = [False]*(n)
        array[judge-1] = True

        for a, b in trust:
            if array[a-1]:
                continue
            else:
                if b == judge:
                    array[a-1] = True
        
        for i in range(n):
            if not array[i]:
                return -1
        
        return judge
        
