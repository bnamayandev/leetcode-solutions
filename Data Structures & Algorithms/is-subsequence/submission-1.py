class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = list(s)


        for c in t[::-1]:
            if stack and stack[-1] == c:
                stack.pop()

        return True if not stack else False