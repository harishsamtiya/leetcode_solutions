class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        def is_prefix(prefix, word):
            n = len(prefix)
            m = len(word)

            if m < n:
                return False
            
            for i in range(n):
                if prefix[i] != word[i]:
                    return False
                
            return True
        
        words = sentence.split()
        for i in range(len(words)):
            if is_prefix(searchWord, words[i]):
                return i+1
        
        return -1