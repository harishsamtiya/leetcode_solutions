class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dia = 0
        area = 0
        for x,y in dimensions:
            new_dia = (x*x) + (y*y)
            if dia < new_dia:
                dia = new_dia
                area = x*y
            elif dia == new_dia:
                area = max(area, x*y)
        return area