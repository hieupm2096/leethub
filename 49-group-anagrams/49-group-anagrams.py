from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for i in strs:
            tmp = ''.join(sorted(i))
            maps[tmp].append(i)
        return maps.values()