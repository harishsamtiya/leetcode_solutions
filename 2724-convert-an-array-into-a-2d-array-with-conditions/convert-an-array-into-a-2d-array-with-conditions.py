class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        myhash = defaultdict(int)

        for num in nums:
            myhash[num] += 1

        result = []
        while myhash:
            temp = []
            todelete = []
            for num, val in myhash.items():
                temp.append(num)
                val -= 1
                myhash[num] = val
                if val == 0:
                    todelete.append(num)
            
            for num in todelete:
                del myhash[num]
            result.append(temp)
        return result
                