class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        letters_count = 0
        word_count = 0
        ch_count = [0]*26


        for word in words:
            for ch in word:
                ch_count[ord(ch) - 97] += 1
                letters_count += 1
            word_count += 1           

        if letters_count/word_count != letters_count//word_count:
            return False
        
        for num in ch_count:
            if num/word_count != num//word_count:
                return False
        
        return True