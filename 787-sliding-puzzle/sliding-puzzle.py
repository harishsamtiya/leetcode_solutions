class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        finalState = [[1,2,3], [4,5,0]]

        
        iInds = [1, -1]
        jInds = [1, -1]
        myset = set()
        q = deque()
        myset.add(str(board))
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    q.append((i, j, 0, board))

        while q:
            i, j , c, state = q.popleft()
            if state == finalState:
                return c

            for p in iInds:
                if 0 <= i+p < 2 :
                    temp = [li.copy() for li in state]
                    temp[i+p][j], temp[i][j] = temp[i][j], temp[i+p][j]
                    if str(temp) not in myset:
                        q.append((i+p, j, c+1, temp))
                        myset.add(str(temp))

            for r in jInds:
                if 0 <= j+r < 3:
                    temp = [li.copy() for li in state]
                    temp[i][j+r], temp[i][j] = temp[i][j], temp[i][j+r]
                    if str(temp) not in myset:
                        
                        q.append((i, j+r, c+1, temp))
                        myset.add(str(temp))
            

        return -1

                    