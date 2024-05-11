class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        array = []
        n = len(wage)

        for i in range(n):
            array.append((wage[i]/quality[i], quality[i]))
        
        result = float('inf')
        array.sort()
        print(array)

        pq = []
        count = 0
        Total_quality = 0
        for wagePerquality, q in array:
            heappush(pq, -q)
            Total_quality += q
            count += 1

            if count > k:
                Total_quality += heappop(pq)
                count -= 1
            
            if count == k:
                result = min(result, wagePerquality * Total_quality)
        return result
