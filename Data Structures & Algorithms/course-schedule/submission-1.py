class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}

        for c, p in prerequisites:
            preMap[c].append(p)
        

        visited = set()
        def dfs(crs):
            nonlocal visited
            if preMap[crs] == []:
                return True

            for pre in preMap[crs]:
                if pre in visited:
                    return False                
                visited.add(pre)
                if not dfs(pre):
                    return False
                preMap[crs] = []
            
            visited = set()
            
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
