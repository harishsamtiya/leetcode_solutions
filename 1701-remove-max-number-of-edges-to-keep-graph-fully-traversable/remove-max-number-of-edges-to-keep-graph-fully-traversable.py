class UnionFind():
    def __init__(self, n=0, li=None):
        if li:
            self.root = li
            self.n = len(li)
        else:
            self.n = n
            self.root = list(range(n))
    
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return False
        
        self.root[rootx] = rooty
        return True

    def isDisconnect(self):
        p = self.find(0)
        for i in range(self.n):
            if p != self.find(i):
                return True
        return False
        
    def getRoots(self):
        return self.root.copy()


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        m = len(edges)
        edgesUsed = 0
        disjointset = UnionFind(n)

        for edgeType, u, v in edges:
            if edgeType == 3:
                if disjointset.union(u-1, v-1):
                    edgesUsed += 1
        
        dsAlice = UnionFind(li=disjointset.getRoots())

        for edgeType, u, v in edges:
            if edgeType == 2:
                if disjointset.union(u-1, v-1):
                    edgesUsed += 1
        if disjointset.isDisconnect():
            return -1

        for edgeType, u, v in edges:
            if edgeType == 1:
                if dsAlice.union(u-1, v-1) :
                    edgesUsed += 1
        if dsAlice.isDisconnect():
            return -1

        return m - edgesUsed