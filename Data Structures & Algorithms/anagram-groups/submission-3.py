class Solution(object):
    def groupAnagrams(self, strs):
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                i = ord(c) - 97
                count[i] += 1
            
            result[tuple(count)].append(s)
        
        return list(result.values())