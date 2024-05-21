class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        pq = []

        for i in range(n):
            pq.append((-((nums[i] ^ k) - nums[i]), i))
        
        heapify(pq)

        while n > 1:
            diff1 , ind1 = heappop(pq)
            diff2, ind2 = heappop(pq)
            diff1, diff2 = -diff1, -diff2
            n -= 2

            if diff1 + diff2 > 0:
                nums[ind1] += diff1
                nums[ind2] += diff2
            else:
                break
                
        return sum(nums)

