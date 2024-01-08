class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mydict = defaultdict(int)

        for num in nums:
            mydict[num] += 1
        result = 0
        for count in mydict.values():
            if count == 1:
                return -1
            elif count == 2:
                 result += 1
            elif count%3 == 0:
                result += count//3
            elif count%3 == 1:
                result += 2 + (count-4)//3
            else:
                result += 1 + (count-2)//3
        return result