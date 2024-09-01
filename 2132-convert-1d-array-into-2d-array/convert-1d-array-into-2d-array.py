class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        total = len(original)

        if n*m != total or total%n != 0:
            return []
        
        result = []
        for i in range(total//n):
            result.append(original[i*n:(i+1)*n])
        
        return result