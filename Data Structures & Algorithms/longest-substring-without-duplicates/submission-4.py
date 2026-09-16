class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = {}
        l = 0
        r = 0
        allmax = 0
        while r < len(s):
            if s[r] in cur and cur[s[r]] >= l:
                l = cur[s[r]] + 1
            cur[s[r]] = r
            allmax = max(r - l + 1, allmax)
            r += 1
        return allmax