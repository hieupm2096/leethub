class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        rs = ''
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                rs += x
            else:
                break
        return rs
                