class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        tree = [[] for _ in range(n)]
        edgeCount = [0]*n

        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)
            edgeCount[x] += 1
            edgeCount[y] += 1
        
        leaves = deque()

        for i in range(n):
            if edgeCount[i] == 1:
                leaves.append(i)
        
        while leaves:
            if n <=2:
                return list(leaves)

            for i in range(len(leaves)):
                leaveNode = leaves.popleft()
                edgeCount[leaveNode] -= 1
                n -= 1
                for neiNode in tree[leaveNode]:
                    edgeCount[neiNode] -= 1

                    if edgeCount[neiNode] == 1:
                        leaves.append(neiNode)