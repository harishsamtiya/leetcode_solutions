class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n, m = len(nums1), len(nums2)
        nums1.sort()
        nums2.sort()
        result = []
        i, j = 0, 0
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                if not (result and result[-1] == nums1[i]):
                    result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return result


        