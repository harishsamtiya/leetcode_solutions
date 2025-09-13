class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootY] = self.parent[rootX]
            return True
        return False

    def isConnected(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return True
        else:
            return False

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        notNeededConnections = 0
        dsu = UnionFind(n)

        for x, y in connections:
            if not dsu.union(x, y):
                notNeededConnections += 1
        

        myset = set()
        for i in range(n):
            rootI = dsu.find(i)
            myset.add(rootI)
        
        connectionsNeeded = len(myset)-1
        if connectionsNeeded > notNeededConnections:
            return -1
        return connectionsNeeded