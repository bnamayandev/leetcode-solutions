class Solution:
    def scoreOfString(self, s: str) -> int:
        score  = 0

        for i in range(len(s) - 1):
            curr_score = abs(ord(s[i]) - ord(s[i+1]))

            score += curr_score
        
        return score
        