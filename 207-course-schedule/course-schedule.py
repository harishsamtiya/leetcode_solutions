class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = defaultdict(int)
        graph = defaultdict(list)

        for v, u in prerequisites:
            degree[v] += 1
            graph[u].append(v)
        
        queue = deque([course for course in range(numCourses) if degree[course] == 0])
        canCompleteCourse = 0

        while queue:
            course = queue.popleft()
            canCompleteCourse += 1

            for newCourse in graph[course]:
                degree[newCourse] -= 1
                if degree[newCourse] == 0:
                    queue.append(newCourse)

        if canCompleteCourse == numCourses:
            return True
        return False