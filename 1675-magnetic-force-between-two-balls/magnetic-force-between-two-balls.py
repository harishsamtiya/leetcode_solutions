class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        l = 0
        r = (max(position) - l+ 1)//(m-1)

        def isPossible(minforce):
            minPosition = position[0] + minforce
            
            count = 1
            for pos in position[1:]:
                if pos >= minPosition:
                    minPosition = pos + minforce
                    count += 1
                    if count == m:
                        return True
            return False

        while l < r:
            mid = r - (r-l)//2

            if isPossible(mid):
                l = mid
            else:
                r = mid - 1
            
        return l