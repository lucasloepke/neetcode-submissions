class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if nums:
            y = nums[0]
            for x in nums[1:]:
                if y == x:
                    return True
                y = x
        return False
                