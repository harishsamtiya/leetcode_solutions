class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mydict = defaultdict(int)

        for num in arr:
            mydict[num] += 1
        
        myset = set()
        for value in mydict.values():
            if value in myset:
                return False
            myset.add(value)
        
        return True