class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        az_chrs = [0]*26

        for ch in s:
            ind = ord(ch) - 97
            az_chrs[ind] += 1

        arr = []

        for i in range(26):
            if az_chrs[i] > 0:
                arr.append((i, az_chrs[i]))

        result = ""

        while arr:
            ind, count = arr.pop()
            ch = chr(ind + 97)

            if count > repeatLimit:
                result += ch*repeatLimit
                count -= repeatLimit

                if not arr:
                    break
                atind, atcount = arr.pop()
                atch = chr(atind + 97)
                atcount -= 1
                result += atch

                if atcount > 0:
                    arr.append((atind, atcount))
            else:
                result += ch*count
                count = 0

            if count > 0:
                arr.append((ind, count))

        return result