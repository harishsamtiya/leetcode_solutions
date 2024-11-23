class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])

        for i in range(m):
            emptyInd = n-1

            for j in range(n-1, -1, -1):
                if box[i][j] == '#':
                    box[i][j] = '.'
                    box[i][emptyInd] = '#'
                    emptyInd -= 1
                elif box[i][j] == '*':
                    emptyInd = j - 1
        
        resultBox = [['.']*m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                resultBox[j][m-1-i] = box[i][j]


        return resultBox
