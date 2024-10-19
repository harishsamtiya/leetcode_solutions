class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        n = floor(log(k, 2))
        arr = [0]
        c = 1

        for i in range(n):
            arr.append(1)
            c += 1
            for j in range(c-2, -1, -1):
                
                if arr[j]:
                 arr.append(0)
                else:
                    arr.append(1)
            c += c- 1


        return str(arr[k-1])