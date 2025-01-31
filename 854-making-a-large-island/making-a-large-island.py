class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        group_area = [0, 0]
        next_group_no = 2

        def find_area(x, y, group_no):
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                grid[x][y] = group_no
                ans = 1 + find_area(x+1, y, group_no) + find_area(x, y+1, group_no) + find_area(x-1, y, group_no) + find_area(x, y-1, group_no)
                return ans
            else:
                return 0
        

        def find_group(x, y):
            if 0 <= x < n and 0 <= y < n and grid[x][y] > 1:
                return grid[x][y]
            else:
                return 0

        max_area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = find_area(i, j, next_group_no)
                    group_area.append(area)
                    max_area = max(area, max_area)
                    next_group_no += 1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    groups = []
                    area = 1
                    for p, q in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                        group = find_group(i+p, j+q)
                        if group not in groups:
                            area += group_area[group]
                            groups.append(group)
                        
                    max_area = max(area, max_area)
        
        
        return max_area

