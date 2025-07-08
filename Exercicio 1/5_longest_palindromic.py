class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        self.start = 0
        self.maxLength = 0

        for i in range(len(s)):
            self.expandAroundCenter(s, i, i)
            self.expandAroundCenter(s, i, i + 1)
        
        return s[self.start : self.start + self.maxLength]

    def expandAroundCenter(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        current_length = right - left - 1

        if current_length > self.maxLength:
            self.maxLength = current_length
            self.start = left + 1