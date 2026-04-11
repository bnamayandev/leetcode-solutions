class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for s in strs:
            val = str(sorted(s))
            hm[val].append(s)
        
        return list(hm.values())