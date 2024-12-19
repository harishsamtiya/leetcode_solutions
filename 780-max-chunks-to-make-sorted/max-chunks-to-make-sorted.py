class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        prevMax = -1

        minvalues = [0]*n

        mini = 11
        for i in range(n-1, -1, -1):
            val = arr[i]
            mini = min(val, mini)
            minvalues[i] = mini

        for i in range(n):
           
            if prevMax < minvalues[i]:
                prevMax = arr[i]
                result += 1
            else:
                prevMax = max(prevMax, arr[i])
            

        return result