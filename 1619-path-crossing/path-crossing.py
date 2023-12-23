class Solution:
    def isPathCrossing(self, path: str) -> bool:
        myset = set()
        x, y = 0, 0
        myset.add((0, 0))
        for dir in path:
            if dir == 'N':
                y += 1
            elif (dir == 'S'):
                y -= 1
            elif dir == 'E':
                x += 1
            else:
                x -= 1
            
            if (x, y) in myset:
                return True
            else:
                myset.add((x,y))

        return False
