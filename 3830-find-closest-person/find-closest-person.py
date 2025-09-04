class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        disA = abs(z-x)
        disB = abs(z-y)
        if disA == disB:
            return 0
        elif disA < disB:
            return 1
        else:
            return 2