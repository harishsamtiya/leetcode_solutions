class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)

        minInd = -1
        maxInd = -1

        mini = 10**4
        maxi = -(mini)

        for i in range(m):
            if mini > arrays[i][0]:
                mini = arrays[i][0]
                minInd = i
            
            if maxi < arrays[i][-1]:
                maxi = arrays[i][-1]
                maxInd = i
    
        
        if minInd != maxInd:
            return maxi - mini
        
        smini = 10**4
        smaxi = -(smini)

        for i in range(m):
            if minInd !=  i:
                if smini > arrays[i][0]:
                    smini = arrays[i][0]
                
                if len(arrays[i]) > 1 and smini > arrays[i][1]:
                    smini = arrays[i][1]
            
            if maxInd != i:
                if smaxi < arrays[i][-1]:
                    smaxi = arrays[i][-1]
                
                if len(arrays[i]) > 1 and smaxi < arrays[i][-2]:
                    smaxi = arrays[i][-2]
        
        return max(smaxi - mini, maxi - smini)
        
