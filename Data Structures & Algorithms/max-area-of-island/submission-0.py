class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            res = 1

            if c < 0 or r < 0 or c>= n or r >= m or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            
            res += dfs(r + 1, c)
            res += dfs(r, c + 1)
            res += dfs(r - 1, c)
            res += dfs(r, c - 1)

            return res
        
        for r in range(m):
            for c in range(n):
                 if grid[r][c] == 1:
                    island = dfs(r,c)
                    maxArea = max(island, maxArea)
        
        return maxArea