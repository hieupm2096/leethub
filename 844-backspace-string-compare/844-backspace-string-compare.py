class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        cs, ct = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0 and (cs > 0 or s[i] == '#'):
                if s[i] == '#':
                    cs += 1
                else:
                    cs -= 1
                i -= 1
            ls = '#' if i < 0 else s[i]
            while j >= 0 and (ct > 0 or t[j] == '#'):
                if t[j] == '#':
                    ct += 1
                else:
                    ct -= 1
                j -= 1
            lt = '#' if j < 0 else t[j]
            if ls != lt:
                return False
            i -= 1
            j -= 1
        return True
        