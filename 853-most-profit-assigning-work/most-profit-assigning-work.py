class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        li = list(zip(profit, difficulty))
        li.sort(reverse=True)
        worker.sort(reverse=True)
        result  = 0
        ind = 0
        n = len(li)
        m = len(worker)
        j = 0
        while j < m:
            while ind < n and li[ind][1] > worker[j]:
                ind += 1

            if ind == n:
                break
            result += li[ind][0]
            j += 1
        
        return result