class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        seats.sort()
        students.sort()

        moves = 0 
        for i in range(n):
            moves += abs(seats[i] - students[i])
        return moves