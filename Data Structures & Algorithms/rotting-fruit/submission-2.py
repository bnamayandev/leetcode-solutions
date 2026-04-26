class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = float("infinity")
        q = deque()
        m, n = len(grid), len(grid[0])
        visit = set()

        def addRoom(r,c):
            if r >= m or c >= n or r < 0 or c < 0 or (r,c) in visit or grid[r][c] != 1:
                return
            visit.add((r,c))
            q.append((r,c))
            grid[r][c] = "#"
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))
        

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c - 1)
                addRoom(r, c + 1)
            
            dist += 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1

        return max(0, dist - 1)