class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pmap = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in pmap:
                stack.append(i)
            elif len(stack) == 0 or pmap[stack.pop()] != i:
                return False
        return len(stack) == 0