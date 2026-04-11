class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()

        while l < r:
            while not s[l].isalpha() and not s[l].isdigit() and l < r:
                l += 1
            
            while not s[r].isalpha() and not s[r].isdigit() and r > l:
                r -= 1
            
            print(s[l], s[r])
            if s[l] != s[r]:
                return False
            
            else:
                l += 1
                r -= 1
        
        return True