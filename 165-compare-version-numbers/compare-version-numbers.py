class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vers1 = version1.split('.')
        vers2 = version2.split('.')

        n, m = len(vers1), len(vers2)

        minLen = min(n, m)
        for i in range(minLen):
            if int(vers1[i]) > int(vers2[i]):
                return 1
            elif int(vers1[i]) < int(vers2[i]):
                return -1
        
        if n == m:
            return 0
        elif n > m:
            for i in range(minLen, n):
                if int(vers1[i]) != 0:
                    return 1
        else:

            for i in range(minLen, m):
                print(vers2[i])
                if int(vers2[i]) != 0:
                    return -1
        return 0

