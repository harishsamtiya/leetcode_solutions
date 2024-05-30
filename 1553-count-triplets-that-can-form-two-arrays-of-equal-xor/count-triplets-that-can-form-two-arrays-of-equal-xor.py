class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefixCnt = defaultdict(int)
        prefixCnt[0] = 1
        prefix_ind_sum = defaultdict(int)
        prefix = 0


        result = 0
        for i in range(n):
            prefix ^= arr[i]

            if prefixCnt[prefix]:
                result += i*prefixCnt[prefix] - prefix_ind_sum[prefix]
            
            prefixCnt[prefix] += 1
            prefix_ind_sum[prefix] += i+1
        
        return result
