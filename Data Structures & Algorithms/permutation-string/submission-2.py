class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        desiredCount = {}
        res = 0

        # make desiredCount
        for c in s1:
            desiredCount[c] = 1 + desiredCount.get(c, 0)
        
        currHashMap = {}
        for l in range(len(s2) - len(s1) + 1):
            if s2[l] not in desiredCount:
                continue
            
            for r in range(l, l+len(s1)):
                currHashMap[s2[r]] = 1 + currHashMap.get(s2[r], 0)
            
            if currHashMap == desiredCount:
                return True
            else:
                currHashMap = {}
            
        
        return False