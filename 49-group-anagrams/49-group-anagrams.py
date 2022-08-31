class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for i in strs:
            tmp = ''.join(sorted(i))
            if tmp in maps:
                maps[tmp].append(i)
            else:
                maps[tmp] = [i]
        return maps.values()