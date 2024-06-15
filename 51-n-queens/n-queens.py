class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["."]*n for _ in range(n)]
        boardAttack = [[0]*n for _ in range(n)]

        result = []

        def placeQueen(i, j):
            board[i][j] = "Q"

            for r in range(i, n):
                boardAttack[r][j] += 1

            k = 1
            while 0 <= i + k < n and 0 <= j - k < n:
                boardAttack[i+k][j-k] += 1
                k += 1

            k = 1
            while 0 <= i + k < n and 0 <= j + k < n:
                boardAttack[i+k][j+k] += 1
                k += 1
        
        def unPlaceQueen(i, j):
            board[i][j] = "."

            for r in range(i, n):
                boardAttack[r][j] -= 1

            k = 1
            while 0 <= i + k < n and 0 <= j - k < n:
                boardAttack[i+k][j-k] -= 1
                k += 1

            k = 1
            while 0 <= i + k < n and 0 <= j + k < n:
                boardAttack[i+k][j+k] -= 1
                k += 1


        def backtrack(row):
            if row == n:
                result.append(["".join(board[i]) for i in range(n)])
            else:
                for i in range(n):
                    if boardAttack[row][i] == 0:
                        placeQueen(row, i)
                        backtrack(row+1)
                        unPlaceQueen(row, i)
                    


        backtrack(0)
        return result
