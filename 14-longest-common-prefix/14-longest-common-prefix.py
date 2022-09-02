class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        rs = ''
        first, last = strs[0], strs[-1]
        print(first)
        print(last)
        for i in range(len(first)):
            if i >= len(last):
                return rs
            if first[i] == last[i]:
                rs += first[i]
            else:
                break
        return rs