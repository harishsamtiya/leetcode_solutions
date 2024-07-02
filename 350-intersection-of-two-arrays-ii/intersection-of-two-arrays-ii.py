class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()

        result = []

        ind = 0
        n = len(nums2)
        for num1 in nums1:

            while ind < n:
                if nums2[ind] < num1:
                    ind += 1
                elif nums2[ind] == num1:
                    result.append(num1)
                    ind += 1
                    break
                else:
                    break
        return result