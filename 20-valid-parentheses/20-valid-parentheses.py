class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['(', '[', '{']
        closes = [')', ']', '}']
        stack = []
        for i in s:
            if i in opens:
                stack.append(i)
            elif i in closes:
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if opens.index(temp) != closes.index(i):
                    return False
        return len(stack) == 0