class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in mapS:
                mapS[s[i]] = 1
            else:
                mapS[s[i]] += 1
            if t[i] not in mapT:
                mapT[t[i]] = 1
            else:
                mapT[t[i]] += 1
        for k, v in mapS.items():
            if k not in mapT:
                return False
            elif mapT[k] != v:
                return False
        return True