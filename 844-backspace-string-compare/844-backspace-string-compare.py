class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks = []
        stackt = []
        for i in s:
            if i != '#':
                stacks.append(i)
            elif len(stacks) > 0:
                stacks.pop()
        for i in t:
            if i != '#':
                stackt.append(i)
            elif len(stackt) > 0:
                stackt.pop()

        return ''.join(stacks) == ''.join(stackt)
        