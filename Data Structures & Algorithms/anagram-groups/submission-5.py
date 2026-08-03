class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            groups_key = str(sorted(s))
            groups[groups_key].append(s)
    
        

        return list(groups.values())