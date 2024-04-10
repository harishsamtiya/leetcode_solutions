class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = [-num for num in deck]
        heapify(deck)

        result = []
        result.append(-heappop(deck))

        while deck:
            result.append(result.pop(0))
            result.append(-heappop(deck))

        result.reverse()
        return result