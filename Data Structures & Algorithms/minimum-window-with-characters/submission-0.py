class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        desired = {} # letter to count
        currWind = defaultdict(int) # letter to indexes, count len()

        for c in t:
            desired[c] = desired.get(c, 0) + 1
        
        l = 0
        res = ""
        resLen = float("inf")

        for r in range(len(s)):
            if s[r] in desired:
                currWind[s[r]] += 1

            while all(currWind.get(k, 0) >= v for k, v in desired.items()):
                if (r - l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                if s[l] in desired:
                    currWind[s[l]] -= 1
                l += 1

        return res