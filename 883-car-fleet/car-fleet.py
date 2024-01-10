class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        li = [(target-p)/s for p, s in sorted(zip(position, speed), reverse=True)]

        next_time = 0
        result  = 0
        for curr_time in li:
            if next_time < curr_time:
                result += 1
            next_time = max(curr_time, next_time)
        return result