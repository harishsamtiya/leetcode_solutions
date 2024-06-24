class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)

        queue = deque()
        result = 0

        for left in range(0, n-k+1):

            while queue and queue[0] < left:
                queue.popleft()
            
            noOfFlips = len(queue)

            if noOfFlips%2 == 1:
                nums[left] = 1 if nums[left] == 0 else 0
            
            if nums[left] != 1:
                result += 1
                nums[left] = 1
                queue.append(left + k -1)


        for left in range(n-k+1, n):
            while queue and queue[0] < left:
                queue.popleft()
            
            noOfFlips = len(queue)

            if noOfFlips%2 == 1:
                nums[left] = 1 if nums[left] == 0 else 0
            
            if nums[left] == 0:
                return -1
            
        return result