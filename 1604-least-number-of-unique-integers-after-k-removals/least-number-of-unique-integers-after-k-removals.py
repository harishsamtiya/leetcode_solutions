class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        mydict = defaultdict(int)

        for num in arr:
            mydict[num] += 1
    
        pq = []
        count = 0

        for value, freq in mydict.items() :
            pq.append((freq, value))
            count += 1

        heapify(pq)

        while k > 0:
            freq, value= heappop(pq)
            if freq > k:
                return count
            count -= 1
            k -= freq

        return count