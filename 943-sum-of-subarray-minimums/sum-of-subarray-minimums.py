class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        summ = 0
        stack = []
        arr.append(0)
        n = len(arr)
        for i in range(n):

            while stack and arr[stack[-1] ] >= arr[i]:
                ind = stack.pop()
                prev_ind = -1
                if stack :
                    prev_ind = stack[-1]
                summ += (ind -prev_ind)*arr[ind]*(i-ind)
            stack.append(i)
        return summ%mod





                


        return sum%mod