class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasArr = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hasArr[ord('a') - ord(s[i].lower())] += 1
            hasArr[ord('a') - ord(t[i].lower())] -= 1


        return hasArr == [0] * 26