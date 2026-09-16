class Solution:
    def isPalindrome(self, s: str) -> bool:
        done = "".join([char for char in s if char.isalnum()]).lower()
        if done == done[::-1]:
            return True
        return False