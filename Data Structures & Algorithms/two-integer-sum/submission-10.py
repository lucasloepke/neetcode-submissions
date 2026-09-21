class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        snums = []
        for i, j in enumerate(nums):
            snums.append([j, i])
        snums.sort()

        l, r = 0, len(nums)-1
        while l < r:
            localsum = snums[l][0] + snums[r][0]
            if localsum < target:
                l += 1
            elif localsum > target:
                r -= 1
            else:
                return sorted([snums[l][1], snums[r][1]])
        