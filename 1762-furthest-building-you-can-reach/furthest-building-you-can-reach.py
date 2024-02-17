class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ind = 1
        n = len(heights)
        pq = [1000000]
        while ind < n and ladders > 0:
            if heights[ind] > heights[ind-1]:
                pq.append(heights[ind] - heights[ind-1])
                ladders -= 1
            ind += 1

        if ind == n:
            return n-1
        
        heapify(pq)

        for i in range(ind, n):
            required_bricks = heights[i] - heights[i-1]
            if required_bricks <= 0:
                continue
            if pq[0] < required_bricks:
                required_bricks = heapreplace(pq, required_bricks)

            if bricks < required_bricks:
                return i -1
            else:
                bricks -= required_bricks

        return n-1
