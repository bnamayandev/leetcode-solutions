class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == -1 or (r,c) in visit:
                return
            
            visit.add((r,c))
            q.append([r,c])
            

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c - 1)
                addRoom(r, c + 1)
            
            dist += 1