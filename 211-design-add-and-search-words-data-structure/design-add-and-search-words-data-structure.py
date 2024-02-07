class WordDictionary:

    def __init__(self):
        self.chars = [(False, None)]*26

    def addWord(self, word: str) -> None:
        n = len(word)
        temp = self.chars

        for i in range(n-1):
            ind = ord(word[i]) - 97

            if temp[ind][1] == None:
                temp[ind] = (temp[ind][0], [(False, None)]*26)
            temp = temp[ind][1]
        ind = ord(word[n-1]) - 97
        temp[ind] = (True, temp[ind][1])


    def search(self, word: str) -> bool:

        def search_word(temp, st):
            n = len(st)
            for i in range(n-1):
                if st[i] == '.':
                    flag = False
                    for j in range(26):
                        if temp[j][1]:
                            if search_word(temp[j][1], st[i+1:]):
                                flag = True
                                break
                    return flag
            
                ind = ord(st[i]) - 97

                if temp[ind][1] is None:
                    return False
                temp = temp[ind][1]
            
            if st[n-1] == '.':
                for i in range(26):
                    if temp[i][0]:
                        return True
                return False
            ind = ord(st[n-1]) - 97
            return temp[ind][0]
        
        return search_word(self.chars, word)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)