class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransoms = {}
        for char in ransomNote:
            if char in ransoms:
                ransoms[char] += 1
            else:
                ransoms[char] = 1
        for char in magazine:
            if char in ransoms:
                ransoms[char] -= 1
        for value in ransoms.values():
            if value > 0:
                return False
        return True