class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        array = [True]*n

        for u, v in edges:
            array[v] = False
        
        ind = -1

        for i in range(n):
            if array[i] == True:
                if ind != -1:
                    return -1
                ind = i
        
        return ind
