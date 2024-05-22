class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def palindrome(start, end):
            l = (end - start)//2 + 1
            for i in range(l):
                if s[start+i] != s[end-i]:
                    return False
            return True
    
        def partition(ind):
            if ind == -1:
                return [[]]
            result = []


            for i in range(ind, -1, -1):
                if palindrome(i, ind):
                    
                    temp = partition(i-1)

                    for li in temp:
                        li.append(s[i: ind+1])
                        result.append(li)

            return result
        
        return partition(n-1)