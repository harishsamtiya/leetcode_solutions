class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        m = len(wordList)

        visited = [False]*m
        wordList.append(beginWord)

        def valid(word1, word2):
            flag = True
            for i in range(n):
                if word1[i] != word2[i]:
                    if flag == False:
                        return False
                    flag = False

            return not flag
        
        queue = deque()
        queue.append((m, 1))

        while queue:
            ind, count = queue.popleft()

            if wordList[ind] == endWord:
                return count
            
            for i in range(m):
                if (not visited[i]) and valid(wordList[ind], wordList[i]):
                    visited[i] = True
                    queue.append((i, count+1))
                
        return 0

