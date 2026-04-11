class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        for i in range(len(s)):
            has = set()

            for j in range(i, len(s)):
                if s[j] in has:
                    break
                
                has.add(s[j])
            
            res = max(res, len(has))

        return res