class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numz = []
        for i, j in enumerate(nums):
            numz.append([j,i])
        numz.sort()
        res = []

        l = 0
        r = len(nums)-1

        while l < r:
            localsum = numz[l][0] + numz[r][0]
            if localsum > target:
                r -= 1
            elif localsum < target:
                l += 1
            else:
                res = sorted([numz[l][1],numz[r][1]])
                break
        return res