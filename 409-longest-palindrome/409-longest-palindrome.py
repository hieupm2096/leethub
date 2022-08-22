class Solution:
    def longestPalindrome(self, s: str) -> int:
        smap = {}
        length = 0
        flag = False
        for c in s:
            if c in smap:
                smap[c] += 1
            else:
                smap[c] = 1
        for value in smap.values():
            if value % 2 == 0:
                length += value
            else:
                flag = True
                if value > 2:
                    length += value - 1
        if flag:
            length += 1
        return length