class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        result = 0
        happiness = [-happy for happy in happiness]
        heapify(happiness)

        for i in range(k):
            happy = -heappop(happiness) - i
            if happy > 0:
                result += happy
            else:
                break
        return result