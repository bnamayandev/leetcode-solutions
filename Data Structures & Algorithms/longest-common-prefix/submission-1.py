class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        while len(strs[0]) > 0:
            currChar = strs[0][0]
            for i in range(1, len(strs)):
                if len(strs[i]) == 0 or strs[i][0] != currChar:
                    return res
                strs[i] = strs[i][1:]
            res += currChar
            strs[0] = strs[0][1:]
        
        return res