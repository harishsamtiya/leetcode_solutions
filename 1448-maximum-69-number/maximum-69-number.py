class Solution:
    def maximum69Number (self, num: int) -> int:
        st = str(num)
        newSt = ''
        flag = True
        for  ch in st:
            if flag and ch == '6':
                newSt = newSt + '9'
                flag = False
            else:
                newSt = newSt + ch
        
        return int(newSt)