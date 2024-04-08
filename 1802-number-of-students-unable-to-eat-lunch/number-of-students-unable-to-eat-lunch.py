class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        oneCount = 0
        n = len(students)

        for num in students:
            if num == 1:
                oneCount += 1
        
        zeroCount = n - oneCount

        for num in sandwiches:
            if num == 1 and oneCount >0:
                oneCount -= 1
            elif num == 0 and zeroCount > 0:
                zeroCount -= 1
            else:
                break
        
        return oneCount + zeroCount
