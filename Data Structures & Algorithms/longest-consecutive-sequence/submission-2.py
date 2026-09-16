class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numz = set(nums)
        # {2,3,4,4,5,10,20}
        start = []
        best = []
        best.append(0)
        if nums:
            for i in numz:
                if i-1 not in numz:
                    start.append(i)
            for i in start:
                x = 1
                while i+1 in numz:
                    x += 1
                    i += 1
                best.append(x)
        return max(best)