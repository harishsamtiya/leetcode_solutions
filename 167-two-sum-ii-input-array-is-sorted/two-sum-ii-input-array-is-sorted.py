class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        i, j = 0, n-1

        while i < j:
            summ = numbers[i] + numbers[j]

            if summ == target:
                return [i+1, j+1]
            elif summ < target:
                i += 1
            else:
                j -= 1
        
        return []