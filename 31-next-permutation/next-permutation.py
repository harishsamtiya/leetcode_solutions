class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        ind = -1
        maxi = -1

        for r in range(n-1, -1, -1):
            if nums[r] < maxi:
                ind = r
                maxi = nums[r]
                break
            maxi = max(maxi, nums[r])

        if ind != -1:
            rep_ind = -1

            for i in range(ind+1, n):
                if nums[i] > nums[ind] and (rep_ind == -1 or nums[rep_ind] > nums[i]):
                    rep_ind = i

            nums[ind], nums[rep_ind] =  nums[rep_ind], nums[ind]

            for i in range(ind+1, n-1):
                min_ind = i
                for j in range(i, n):
                    if nums[min_ind] > nums[j]:
                        min_ind = j
                nums[i], nums[min_ind] = nums[min_ind], nums[i]
        else:
            nums.sort()

