class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        nv1 = len(v1)
        nv2 = len(v2)

        n = max(nv1, nv2)

        for i in range(n):
            if i < nv1:
                num1 = int(v1[i])
            else:
                num1 = 0
            
            if i < nv2:
                num2 = int(v2[i])
            else:
                num2 = 0
            

            if num1 > num2:
                return 1
            elif num2 > num1:
                return -1

        return 0