class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        ticketsK = tickets[k]
        n = len(tickets)

        for i in range(n):
            if i == k:
                time += ticketsK
                ticketsK -= 1
            else:
                time += min(tickets[i], ticketsK)
        
        return time