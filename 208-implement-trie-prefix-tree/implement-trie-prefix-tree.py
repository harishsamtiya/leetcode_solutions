class Trie:
    
    def __init__(self):
        self.chars = [(False, None)]*26

    def insert(self, word: str) -> None:
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
        n = len(word)
        temp = self.chars
        for i in range(n-1):
            ind = ord(word[i]) - 97

            if temp[ind][1] == None:
                return False
            temp = temp[ind][1]
        
        ind = ord(word[n-1]) - 97
        return temp[ind][0]


    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        temp = self.chars
        for i in range(n-1):
            ind = ord(prefix[i]) - 97

            if temp[ind][1] == None:
                return False
            temp = temp[ind][1]
        ind = ord(prefix[n-1]) - 97

        return temp[ind][0] or temp[ind][1]

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)