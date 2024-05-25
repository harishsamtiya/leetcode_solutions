class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]: 
        trie = [None]*26
        trie.append(False)

        def insert(word):
            node = trie

            for ch in word:
                chInd = ord(ch) - 97
                if node[chInd] == None:
                    temp = [None]*26
                    temp.append(False)
                    node[chInd] = temp
                node = node[chInd]
            
            node[26] = True

        for word in wordDict:
            insert(word)
        
        n = len(s)
        stack = [(0, "")]
        result = []

        while stack:
            ind, st = stack.pop()
            if ind == n:
                result.append(st)
            else:
                node = trie
                for i in range(ind, n):
                    chInd = ord(s[i]) - 97
                    if node[chInd]:
                        if node[chInd][26]:
                            if st != "":
                                stack.append((i+1, st + " " + s[ind: i+1]))
                            else:
                                stack.append((i+1, s[ind: i+1]))
                        node = node[chInd]
                    else:
                        break

        return result