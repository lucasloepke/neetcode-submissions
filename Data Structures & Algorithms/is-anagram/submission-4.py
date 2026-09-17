class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss, tt = sorted(s), sorted(t)
        if ss == tt:
            return True
        return False