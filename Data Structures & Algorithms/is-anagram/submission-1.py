class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sr = "".join(sorted(s))
        st = "".join(sorted(t))
        if st == sr:
            return True
        return False