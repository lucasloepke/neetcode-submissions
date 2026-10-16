class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1,2,3,2,2]
        for i in nums:
            val = nums[abs(i)-1]
            if val < 0:
                return abs(i)
            else:
                nums[abs(i)-1] = -val #-1,-4
        return -1