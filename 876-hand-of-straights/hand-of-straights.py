class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n%groupSize:
            return False
        
        if groupSize == 1:
            return True

        hand.sort()
        de = deque()

        for val in hand:
            if de:
                topCard, count = de.popleft()
                if topCard + 1 == val:
                    if count + 1 < groupSize:
                        de.append((val, count+1)) 
                elif topCard == val:
                    de.appendleft((topCard, count)) 
                    de.appendleft((val, 1))
                else:
                    return False
            else:
                de.append((val, 1))


        if de:
            return False
        return True