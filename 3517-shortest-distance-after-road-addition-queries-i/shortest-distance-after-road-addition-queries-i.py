class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        connections = [[] for _ in range(n)]
        answers = []

        def bfs():
            visited = set()

            q = deque()
            q.append((0, 0))
            visited.add(0)

            while q:
                node, steps = q.popleft()

                if node == n-1:
                    return steps
                
                if connections[node] :
                    for v in connections[node]:
                        q.append((v, steps+1))
                        visited.add(v)

                if (node+1) not in visited:
                    q.append((node+1, steps+1))
                    visited.add(node+1)
                
            
            return n-1

        
        for u, v in queries:
            connections[u].append(v)

            answers.append(bfs())
        
        return answers