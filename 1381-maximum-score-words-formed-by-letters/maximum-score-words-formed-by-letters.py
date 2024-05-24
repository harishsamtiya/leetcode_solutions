class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        self.lettersCount = [0]*26
        
        for ch in letters:
            self.lettersCount[ord(ch)-97] += 1
        

        def backtrack(ind):
            if ind == n:
                return 0
            
            notInclude = backtrack(ind+1)
            temp = self.lettersCount.copy()
            
            scoreInd = 0 
            for ch in words[ind]:
                chInd = ord(ch)-97
                self.lettersCount[chInd] -= 1
                scoreInd += score[chInd]
                if self.lettersCount[chInd] < 0:
                    self.lettersCount = temp
                    return notInclude
            
            include = backtrack(ind+1) + scoreInd
            self.lettersCount = temp

            return max(include, notInclude)
        
        return backtrack(0)