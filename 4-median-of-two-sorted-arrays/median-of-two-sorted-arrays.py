class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n2 < n1:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        
        l, r = 0, n1-1
        n = n1 + n2
        half = n//2

        while True:
            i = (l+r)//2
            j = half - i-2

            lefti = nums1[i] if i>= 0 else float('-inf')
            righti = nums1[i+1] if i+1<n1  else float('inf')

            leftj = nums2[j] if j>= 0 else float('-inf')
            rightj = nums2[j+1]  if j+1<n2 else float('inf')

            if lefti <= rightj and leftj <= righti:
                if n%2:
                    return min(righti, rightj)
                else:
                    return (max(lefti, leftj) + min(righti, rightj))/2
            elif lefti > rightj:
                r = i -1
            else:
                l = i + 1 
