class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(key)
        m = len(ring)
        pq = [(0, 0, 0)]

        memo = [[float('inf')]*(m) for _ in range(n+1)]

        while pq:
            moves, curr, tar = heappop(pq)
            if tar == n:
                return moves

            ch = key[tar]
            moves += 1

            if ch == ring[curr]:
                heappush(pq, (moves, curr, tar+1))
            else:

                leftInd = -1
                for i in range(curr-1, -1, -1):
                    if ch == ring[i]:
                        leftInd = i
                        break
                
                rightInd = -1
                for i in range(curr+1, m):
                    if ch == ring[i]:
                        rightInd = i
                        break
                
                if leftInd == -1:
                    for i in range(m-1, rightInd, -1):
                        if ch == ring[i]:
                            leftInd = i
                            break
                
                if rightInd == -1:
                    for i in range(0, leftInd):
                        if ch == ring[i]:
                            rightInd = i
                            break

                if leftInd != -1:
                    dis = abs(curr-leftInd)
                    if memo[tar+1][leftInd] > moves + min(dis, m-dis):
                        memo[tar+1][leftInd] = moves + min(dis, m-dis)
                        heappush(pq, (moves + min(dis, m-dis), leftInd, tar+1))
                
                if rightInd != -1 and leftInd != rightInd:
                    dis = abs(curr - rightInd)
                    if memo[tar+1][rightInd] > moves + min(dis, m-dis):
                        memo[tar+1][rightInd] = moves + min(dis, m-dis)
                        heappush(pq, (moves+min(dis, m-dis), rightInd, tar+1))