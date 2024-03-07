class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        chars = [0]*26

        for ch in tasks:
            ind = ord(ch) - 65
            chars[ind] += 1
        
        pq = []
        for val in chars:
            if val:
                pq.append(-val)
    
        heapify(pq)
        time = 0
        queue = []
        while pq or queue:
            time += 1
            if pq:
                val = heappop(pq)
                val += 1
                if val:
                    queue.append((time+n, val))
            if queue and queue[0][0] <= time:
                tillTime, val = queue.pop(0)
                heappush(pq, val)


        return time
            