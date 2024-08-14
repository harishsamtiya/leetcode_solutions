class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, 10**6
        k -= 1
        def pairCount(mid):
            count = 0
            for i in range(n):
                l, r = i, n-1
                val = nums[i]
                
                while l < r:
                    m = r - (r - l)//2
                    if (nums[m] - val) > mid:
                        r = m - 1
                    else:
                        l = m
                             
                count += l -i
                     
            return count

        def isPossible(num):

            for i in range(n):

                l, r = i+1, n-1

                while l <= r:
                    m = (l+r)//2

                    val = nums[m] - nums[i]
                    if val == num:
                        return True
                    elif val > m:
                        r = m -1
                    else:
                        l = m + 1
            return False

        while l <= r:
            mid = (l + r)//2

            smallMidpair = pairCount(mid-1)

            if smallMidpair == k:
                if isPossible(mid):
                    return mid
                else:
                    if (not isPossible(l)) or (pairCount(l-1) != k):
                        l += 1
                    elif (not isPossible(r)) or (pairCount(r-1) != k):
                        r -= 1
                    else:
                        print("I don't know")
                        return -1
            elif smallMidpair > k:
                r = mid - 1
            else:
                l = mid + 1
        
        return r
            