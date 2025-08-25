class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        n, m = len(mat), len(mat[0])
        row, col = 0, 0
        dirs = True # 1 up , 0 down
        cnt  = 0

        def Valid(row, col):
            if (row < 0 or row >= n) or (col < 0 or col >= m):
                return False
            return True

            
        while cnt < n*m:
            curr_row = row
            curr_col = col
            result.append(mat[row][col])
            cnt += 1
            if dirs:
                row -= 1
                col += 1
            else:
                row += 1
                col -= 1

            if not Valid(row, col):
                if dirs:
                    if Valid(curr_row, curr_col+1):
                        row, col = curr_row, curr_col + 1
                    else:
                        row, col = curr_row + 1, curr_col
                else:
                    if Valid(curr_row+1, curr_col):
                        row, col = curr_row + 1, curr_col
                    else:
                        row, col = curr_row , curr_col + 1
                dirs = not dirs

        return result
