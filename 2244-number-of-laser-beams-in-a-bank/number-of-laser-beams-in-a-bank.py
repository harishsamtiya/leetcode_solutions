class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        beams = 0
        for row in bank:
            count = 0
            for cam in row:
                if cam == '1':
                    count += 1
            if count:
                beams += prev*count
                prev = count
        return beams