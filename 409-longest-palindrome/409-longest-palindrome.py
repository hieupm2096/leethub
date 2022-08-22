class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        flag = False
        for value in collections.Counter(s).values():
            if value % 2 == 0:
                length += value
            else:
                flag = True
                if value > 2:
                    length += value - 1
        if flag:
            length += 1
        return length