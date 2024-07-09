class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        waitTime = 0
        idle = 0
        for arr, time in customers:
            if arr < idle:
                waitTime += idle - arr
            else:
                idle = arr
            idle += time
            waitTime += time

        return waitTime/n