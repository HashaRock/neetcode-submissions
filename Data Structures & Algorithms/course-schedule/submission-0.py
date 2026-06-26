class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deps = {i : [] for i in range(numCourses)}

        for course, req in prerequisites:
            deps[course].append(req)

        visited = set()

        def dfs(c):
            if c in visited:
                return False
            if deps[c] == []:
                return True
            
            visited.add(c)

            for req in deps[c]:
                if not dfs(req):
                    return False
            
            visited.remove(c)
            deps[c] = []
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True