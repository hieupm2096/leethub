class Solution:
    def getKey(self, word: str) -> tuple:
        chars = [0] * 26
        for char in word:
            chars[ord(char) - ord('a')] += 1
        return tuple(chars)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for i in strs:
            tmp = self.getKey(i)
            if tmp in maps:
                maps[tmp].append(i)
            else:
                maps[tmp] = [i]
        return maps.values()