class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sett = set()
        for i in nums:
            if i not in sett:
                sett.add(i)
            else:
                return i