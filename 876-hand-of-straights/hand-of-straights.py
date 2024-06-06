class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n%groupSize:
            return False
        
        
        mydict = defaultdict(int)
        pq = []
        for num in hand:
            if num not in mydict:
                pq.append(num)
            mydict[num] += 1

        heapify(pq)

        while mydict:
            num = heappop(pq)
            
            while mydict[num] == 0 and pq:
                num = heappop(pq)

            count = mydict[num]
            del mydict[num]
            if not pq and count == 0:
                break
            for card in range(num+1, num + groupSize):
                if card not in mydict or mydict[card] < count:
                    return False
                
                mydict[card] -= count




        return True   
            