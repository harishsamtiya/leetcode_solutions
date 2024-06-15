class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        digitsToletters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


        represent = [""]
        for digit in digits:
            digit = int(digit)
            ind = digit - 2

            temp = []
            for ch in digitsToletters[ind]:
                for st in represent:
                    temp.append(st+ch)
            represent = temp

        return represent
            