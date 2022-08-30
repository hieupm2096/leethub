class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        sub = 0
        for i in range(len(s)):
            result += roman[s[i]]
            if i + 1 < len(s):
                if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                    sub += 2
                elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                    sub += 20
                elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                    sub += 200
        return result - sub
                