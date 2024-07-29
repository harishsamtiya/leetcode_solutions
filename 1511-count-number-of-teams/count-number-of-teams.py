class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)
        li = []

        for i in range(n):
            minValues = 0
            maxValues = 0

            for j in range(i+1, n):
                if rating[i] > rating[j]:
                    minValues += 1
                elif rating[j] > rating[i]:
                    maxValues += 1
            li.append((minValues, maxValues))
        
        count = 0

        for i in range(n):
            for j in range(i+1, n):

                if rating[i] == rating[j]:
                    continue
                elif rating[i] > rating[j]:
                    count += li[j][0]
                else:
                    count += li[j][1]

        return count
            