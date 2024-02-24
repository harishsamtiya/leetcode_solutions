class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        meetings.sort(key=lambda x : x[2])
        whoKnows = [False]*(n)
        whoKnows[0] = True
        whoKnows[firstPerson] = True
        prev = 0

        def dfs(i):
            temp = graph[i]
            del graph[i]
            for j in temp:
                whoKnows[j] = True
                dfs(j)

        for x, y, t in meetings:
            if t != prev:   
                graph = defaultdict(list)

            if whoKnows[x] and not whoKnows[y]:
                whoKnows[y] = True
                dfs(y)


            elif whoKnows[y] and not whoKnows[x]:
                whoKnows[x] = True
                dfs(x)
            
            if not (whoKnows[x] or  whoKnows[y]):
                graph[x].append(y)
                graph[y].append(x)
            prev = t

        result = []
        for i in range(n):
            if whoKnows[i]:
                result.append(i)
        return result




        
