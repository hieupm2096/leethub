class Solution:
    def isPalindrome(self, s: str) -> bool:
        re = ''.join(e for e in s if e.isalnum()).lower()
        for i in range(0, len(re) // 2):
            if re[i] != re[len(re) - 1 - i]:
                return False
        return True