# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.firstBadVersionFn(1, n)
    
    def firstBadVersionFn(self, start: int, end: int) -> int:
        if start == end:
            return start
        mid = start + (end - start) // 2
        if isBadVersion(mid):
            end = mid
            return self.firstBadVersionFn(start, end)
        else:
            start = mid + 1
            return self.firstBadVersionFn(start, end)