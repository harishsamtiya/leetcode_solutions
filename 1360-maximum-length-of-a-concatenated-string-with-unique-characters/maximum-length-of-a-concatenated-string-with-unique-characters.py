class Solution:
    def maxLength(self, arr: List[str]) -> int:
        sets = []

        for st in arr:
            temp = set()
            flag = True
            for ch in st:
                if ch in temp:
                    flag = False
                    break
                temp.add(ch)
            if flag:
                sets.append(temp)
        
        n = len(sets)
        


        def backtrack(curr_set,ind):
            if ind == n:
                return len(curr_set)
            ans = backtrack(curr_set, ind+1)
            if curr_set.isdisjoint(sets[ind]):
                ans  = max(backtrack(curr_set.union(sets[ind]), ind+1) , ans)
            return ans
        return backtrack(set(), 0)

        
