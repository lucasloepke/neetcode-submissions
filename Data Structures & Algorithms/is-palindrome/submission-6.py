class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join([x for x in s if x.isalnum()]).lower()
        return cleaned == cleaned[::-1]