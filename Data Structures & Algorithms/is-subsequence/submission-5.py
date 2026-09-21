class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #allowed = set(s)
        #ft = "".join([char for char in t if char in allowed])
        i = j = 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i+=1
            j+=1

        return i == len(s)