class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {} # value to index
        if not s:
            return 0

        res = 1
        l = 0

        for r in range(len(s)):
            if s[r] in hashmap:
                ind = hashmap[s[r]]
                del hashmap[s[r]]
                hashmap[s[r]] = r
                l = max(ind + 1, l ) # check this

            hashmap[s[r]] = r
            res = max(res, r-l + 1)

        return res

