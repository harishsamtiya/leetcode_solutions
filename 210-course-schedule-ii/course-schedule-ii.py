class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        dependedCourses = [0]*numCourses
        for second, first in prerequisites:
            graph[first].append(second)
            dependedCourses[second] += 1
        
        count = 0
        result = []
        for i in range(numCourses):
            if dependedCourses[i] == 0:
                result.append(i)
                count += 1

        while count < numCourses:
            flag = True
            for i in range(numCourses):
                if dependedCourses[i] == 0:
                    dependedCourses[i] = -1
                    flag = False
                    for course in graph[i]:
                        dependedCourses[course] -= 1
                        if dependedCourses[course] == 0:
                            result.append(course)
                            count += 1 
            if flag:
                return []
        return result
        
        