class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in times:
            graph[u-1].append((v-1, w))
        

        
        pq = [(0, k-1)]
        time = [float('inf') for _ in range(n)]
        time[k-1] = 0

        while pq:
            w, u = heapq.heappop(pq)

            for v, w_v in graph[u]:
                new_w = w_v + w
                if new_w < time[v]:
                    time[v] = min(time[v], new_w)
                    heapq.heappush(pq, (new_w, v))
        
        
        if float('inf') in time:
            return -1
        return max(time)
