class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        n = len(nums) + 1
        nums.append(-1*10**4)
        self.li = nums[0:k]
        heapq.heapify(self.li)

        print(self.li)
        for i in range(k, n):
            if nums[i] > self.li[0]:
                heapq.heapreplace(self.li, nums[i])

    def add(self, val: int) -> int:
        if val > self.li[0]:
            heapq.heapreplace(self.li, val)
        return self.li[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)