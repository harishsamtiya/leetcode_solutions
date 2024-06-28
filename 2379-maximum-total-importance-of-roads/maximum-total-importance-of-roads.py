class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0]*n
        
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
        
        li = list(enumerate(degree))
        li.sort(key = lambda x: x[1], reverse=True)

        for i in range(n):
            pos = li[i][0]
            degree[pos] = n - i
        del(li)
        
        summ = 0

        for u, v in roads:
            summ += degree[u] + degree[v]

        return summ
