class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        n = len(queries)
        m = len(items)
        queries = list(enumerate(queries))
        queries.sort(key=lambda x:x[1])
        print(queries)

        result = [0]*n
        beauty = 0
        i = 0

        for ind, currPrice in queries:
            while i < m and items[i][0] <= currPrice:
                beauty = max(items[i][1], beauty)
                i += 1
            result[ind] = beauty
        return result

