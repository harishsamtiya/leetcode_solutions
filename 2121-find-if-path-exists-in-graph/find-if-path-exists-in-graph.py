class UnionSet:
    
    def __init__(self, n):
        self.root = [i for  i in range(n)]
        self.rank = [1]*n

    def find(self, x):
        if self.root[x] == x:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] >= self.rank[rootY]:
            self.root[rootY] = rootX
            if self.rank[rootX] == self.rank[rootY]:
                self.rank[rootX] += 1
        else:
            self.root[rootX] = rootY
        
        return True
    
    def connected(self, x, y):
        if self.find(x) == self.find(y):
            return True
        return False


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
         
        disjointSet = UnionSet(n)

        for x,y in edges:
            if disjointSet.union(x, y):
                if disjointSet.connected(source, destination):
                    return True
        return disjointSet.connected(source, destination)
