class Solution:
    def trap(self, height: List[int]) -> int:
        maxHeight = 0
        i, j = 0, len(height)-1
        trapWater = 0
        
        while i < j:
            maxHeight = max(maxHeight, min(height[i], height[j]))
            if height[i] > height[j]:
                trapWater += maxHeight - min(maxHeight, height[j])
                j -= 1
            else:
                trapWater += maxHeight - min(maxHeight, height[i])
                i += 1

        return trapWater