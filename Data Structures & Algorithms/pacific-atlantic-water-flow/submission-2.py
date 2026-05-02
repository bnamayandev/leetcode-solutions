class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        touchP = set()
        touchA = set()
        res = []

        def dfs(r,c,currHeight, ocean):
            if r < 0 or c < 0 or r >= m or c >= n or (r,c) in ocean:
                return
            
            if heights[r][c] >= currHeight:
                ocean.add((r,c))
                dfs(r - 1,c, heights[r][c], ocean)
                dfs(r + 1,c, heights[r][c], ocean)
                dfs(r,c - 1, heights[r][c], ocean)
                dfs(r,c + 1, heights[r][c], ocean)
            
            return
            


        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dfs(r,c, -1, touchP)
                if r == m - 1 or c == n - 1:
                    dfs(r,c, 0, touchA)

        for p in touchP:
            if p in touchA:
                res.append(p)
        return res