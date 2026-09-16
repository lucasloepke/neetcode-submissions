class Solution:
    def isPalindrome(self, s: str) -> bool:
        fs = (("".join(filter(str.isalnum, s))).lower())
        if fs == fs[::-1]:
            return True
        return False