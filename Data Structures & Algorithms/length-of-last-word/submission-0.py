class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = list(s.split(" "))
        
        i = len(words) - 1
        while len(words[i]) < 1:
            i -= 1
        return len(words[i])