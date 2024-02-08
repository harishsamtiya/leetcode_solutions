class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*stone for stone in stones]
        heapify(stones)
        n = len(stones)

        while n > 1:
            stone1 = heappop(stones)
            stone2 = heappop(stones)
            n -= 2
            if stone1 != stone2:
                heappush(stones, (-1)*abs(stone1 - stone2))
                n += 1
        if stones:
            return (-1)*stones[0]
        return 0