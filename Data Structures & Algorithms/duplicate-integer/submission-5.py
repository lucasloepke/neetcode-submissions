class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        while nums:
            prev = nums[0]
            for i in range(len(nums)):
                if (nums[i] == prev) and (i != 0):
                    return True
                prev = nums[i]
            return False
        return False