class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for index, value in enumerate(nums):
            A.append([value,index])
        A.sort()

        l = 0
        r = len(nums)-1
        while l < r:
            if A[r][0] + A[l][0] < target:
                l += 1
            elif A[r][0] + A[l][0] > target:
                r -= 1
            else:
                return sorted([A[l][1], A[r][1]])
        return []