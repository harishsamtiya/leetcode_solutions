class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        if '0000' in deadends:
            return -1

        if target == '0000':
            return 0
        queue = deque([('0000', 0)])


        

        while queue:
            num, moves = queue.popleft()
            moves += 1
            for i in range(4): 
                prev = num[0:i] + str((int(num[i]) + 9)%10) + num[i+1:] 
                Next = num[0:i] + str((int(num[i]) + 11)%10) + num[i+1:]

                if prev == target or Next == target:
                    return moves
                
                if prev not in deadends:
                    queue.append((prev, moves))
                    deadends.add(prev)
                
                if Next not in deadends:
                    queue.append((Next, moves))
                    deadends.add(Next)

        return -1