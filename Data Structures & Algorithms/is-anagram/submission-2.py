class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort = sorted(s)
        tort = sorted(t)

        if sort == tort:
            return True
        return False