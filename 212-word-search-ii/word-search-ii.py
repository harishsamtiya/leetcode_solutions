
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        TrieNode = [(None, False) for _ in range(26)]
        
        def add(word, TrieNode):
            node = TrieNode
            prev = None

            for ch in word:
                prev = node
                ind = ord(ch) - 97

                if not node[ind][0]:
                    newNode = [(None, False) for _ in range(26)]
                    node[ind] = (newNode, False)
                node = node[ind][0]
                    
            prev[ind] = (prev[ind][0], True)

        
        for word in words:
            add(word, TrieNode)

        m = len(board)
        n = len(board[0])
        used = [[False]*n for _ in range(m)]
        def dfs(i, j, node):
            if i < 0 or i >= m or j < 0 or j >= n or used[i][j]:
                return None
            used[i][j] = True
            ind = ord(board[i][j]) - 97

            if node[ind][0]:
                result = []
                if node[ind][1]:
                    result.append(board[i][j])
                

                up = dfs(i-1, j, node[ind][0])
                if up:
                    for suffix in up:
                        result.append(board[i][j] + suffix)

                down = dfs(i+1, j, node[ind][0])
                if down:
                    for suffix in down:
                        result.append(board[i][j] + suffix)

                left = dfs(i, j-1, node[ind][0])
                if left:
                    for suffix in left:
                        result.append(board[i][j] + suffix)

                right = dfs(i, j+1, node[ind][0])
                if right:
                    for suffix in right:
                        result.append(board[i][j] + suffix)
                used[i][j] = False
                if result:
                    return result
                return None
            used[i][j] = False
            return None

        result = []

        for i in range(m):
            for j in range(n):
                words = dfs(i, j, TrieNode)
                if words:
                    for word in words:
                        result.append(word)
        return  list(set(result)) 