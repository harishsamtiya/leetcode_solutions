class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        dependedCourses = [0]*numCourses
        for second, first in prerequisites:
            graph[first].append(second)
            dependedCourses[second] += 1
        
        count = 0
        for val in dependedCourses:
            if val == 0:
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
                            count += 1 
            if flag:
                return False
        return True
        
        

            
