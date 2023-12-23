class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = defaultdict(int)
        p = []
        for num in nums:
            mydict[num] += 1

        for x, y in mydict.items():
            p.append((-y, x))

        heapify(p)
        result = []
        for i in range(k):
            y, x = heappop(p)
            result.append(x)
        return result