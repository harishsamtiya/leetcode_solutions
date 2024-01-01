class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1

        vol = 0
        sea_level = 0

        while l < r:

            if height[l] <= sea_level:
                vol += sea_level - height[l]
                l += 1
            elif height[r] <= sea_level:
                vol += sea_level - height[r]
                r -= 1
            else:
                sea_level = min(height[l], height[r])
        return vol