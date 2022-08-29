class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = b.rjust(len(a), '0')
        else:
            a = a.rjust(len(b), '0')
        d = 0
        result = ''
        for i in range(len(a) - 1, -1, -1):
            c = d + int(a[i]) + int(b[i])
            if c == 3:
                result += '1'
                d = 1
            elif c == 2:
                result += '0'
                d = 1
            elif c == 1:
                result += '1'
                d = 0
            else:
                result += '0'
                d = 0
        if d == 1:
            result += '1'
        return result[::-1]