class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        array = [0]*n
        meetings.sort()

        booked = []
        freeRooms = [i for i in range(n)]


        for start, end in meetings:

            while booked:
                freeAt, roomNo = booked[0]
                if freeAt <= start:
                    heappush(freeRooms, roomNo)
                    heappop(booked)
                else:
                    break
            
            if freeRooms:
                freeRoom = heappop(freeRooms)
                heappush(booked, (end, freeRoom))
            else:
                freeAt, freeRoom = heappop(booked)
                heappush(booked, (freeAt + end - start, freeRoom))

            array[freeRoom] += 1
        
        ind = 0
        for i in range(n):
            if array[i] > array[ind]:
                ind = i
        return ind