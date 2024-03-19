class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ch_array = [0]*26

        for ch in tasks:
            ind = ord(ch)-65
            ch_array[ind] += 1

        pq = []

        for freq in ch_array:
            if freq > 0:
                pq.append(-freq)
        
        heapify(pq)
        time = 0
        queue = []

        while pq or queue:
            if pq:
                val = heappop(pq)
            else:
                tillTime, val = queue.pop(0)
                time = tillTime + 1

            val += 1

            if val != 0:
                queue.append((time+n, val))
            
            if queue and queue[0][0] == time:
                tillTime, val = queue.pop(0)
                heappush(pq, val)
            time += 1
            
        return time

