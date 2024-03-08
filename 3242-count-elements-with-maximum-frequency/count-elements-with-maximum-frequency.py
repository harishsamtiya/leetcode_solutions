class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums.sort()
        
        max_freq = 0
        count = 0
        prev = 0
        freq = 0
        for num in nums:
            if num == prev:
                freq += 1
            else:
                if freq == max_freq:
                    count += freq
                elif freq > max_freq:
                    max_freq = freq
                    count = freq
                prev = num
                freq = 1
 
        if freq == max_freq:
            count += freq
        elif freq > max_freq:
            max_freq = freq
            count = freq
        return count
            
                    