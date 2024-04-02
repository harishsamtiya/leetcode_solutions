class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)

        if n1 != n2:
            return False
        
        domain = [-1]*256
        codomain = [-1]*256

        for i in range(n1):
            ind = ord(s[i])

            value = ord(t[i])
            print(ind, value, domain[ind])
            if domain[ind] == -1:
                if codomain[value] != -1 and codomain[value] != ind:
                    return False
                codomain[value] = ind
                domain[ind] = value
            elif domain[ind] != value:
                return False
            
        return True