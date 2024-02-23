class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for sr, ds, pr in flights:
            graph[sr].append((ds, pr))
        
        memo = {}

        def dfs(sr, ko):
            if ko > k:
                if sr == dst:
                    return 0
                return float('inf')

            if (sr, ko) in memo:
                return memo[(sr, ko)]

            if sr == dst:
                return 0

            ans = float('inf')
            for ds, pr in graph[sr]:
                temp = dfs(ds, ko+1)
                if temp != float('inf'):
                    ans = min(temp + pr, ans)
            
            memo[(sr, ko)] = ans
            return ans
        
        result = dfs(src, 0)
        return -1 if result == float('inf') else result
