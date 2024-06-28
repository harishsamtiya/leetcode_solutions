class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0]*n

        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
        
        degree.sort()
        
        summ = 0
        for i in range(n):
            summ += degree[i] * (i+1)

        return summ
