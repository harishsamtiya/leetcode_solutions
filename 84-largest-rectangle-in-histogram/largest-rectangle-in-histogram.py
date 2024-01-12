class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        area = 0
        for i in range(n):
            new_i = i
            while stack and stack[-1][0] > heights[i]:
                height, ind = stack.pop()
                area = max(area, height*(i-ind))
                new_i = ind
            
            stack.append((heights[i], new_i))
        
        while stack:
            height, ind = stack.pop()
            area = max(area, height*(n-ind))
        return area