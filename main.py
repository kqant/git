class Solution:
    def romanToInt(self, s: str) -> int:
        digit = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] == 'M':
                s[i] = 1000
            elif s[i] == 'D':
                s[i] = 500
            elif s[i] == 'C':
                s[i] = 100
            elif s[i] == 'L':
                s[i] = 50
            elif s[i] == 'X':
                s[i] = 10
            elif s[i] == 'V':
                s[i] = 5
            elif s[i] == 'I':
                s[i] = 1
        digit += s[-1]
        for i in range(len(s)-1, 0, -1):
            if s[i-1] >= s[i]:
                digit += s[i-1]
            else:
                digit -= s[i-1]
        return digit

