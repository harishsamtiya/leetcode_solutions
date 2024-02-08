class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        def distance(x, y):
            return -((x*x + y*y)**(0.5))

        pq = [(distance(x, y), [x, y]) for x, y in points[:k]]

        heapify(pq)

        for x,y in points[k:]:
            dis = distance(x, y)
            if dis > pq[0][0]:
                heapreplace(pq,(dis, [x,y]))
        
        return [point for _, point in pq]
