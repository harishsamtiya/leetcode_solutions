class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        array = list(zip(score, list(range(n))))
        array.sort(reverse=True)
        print(array)
        if n > 0:
            score[array[0][1]] = "Gold Medal"
        
        if n > 1:
            score[array[1][1]] = "Silver Medal"
        
        if n > 2:
            score[array[2][1]] = "Bronze Medal"
        
        for i in range(3, n):
            score[array[i][1]] = str(i+1)

        return score