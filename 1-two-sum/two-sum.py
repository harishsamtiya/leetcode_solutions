class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myhash = dict()
        n = len(nums)

        for i in range(n):
            myhash[nums[i]] = i

        for i in range(n):
            remain = target - nums[i]
            if remain in myhash and myhash[remain] != i:
                return [i, myhash[remain]]
        return []
        