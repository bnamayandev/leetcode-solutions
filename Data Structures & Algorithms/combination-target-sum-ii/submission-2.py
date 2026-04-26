class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        res = []
        currSet = []
        visit = set()

        def dfs(i, curSum):
            if curSum == target:
                res.append(currSet.copy())
                return
            
            if i >= len(candidates) or curSum > target:
                return
            
            currSet.append(candidates[i])
            dfs(i + 1, curSum + candidates[i])

            currSet.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curSum)
        
        dfs(0,0)
        return res