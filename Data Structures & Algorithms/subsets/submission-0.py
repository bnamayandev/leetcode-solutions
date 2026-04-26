class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        currSet = []
        def dfs(i):
            if i >= len(nums):
                res.append(currSet.copy())
                return

            currSet.append(nums[i])
            dfs(i + 1)

            currSet.pop()
            dfs(i + 1)

        dfs(0)
        return res