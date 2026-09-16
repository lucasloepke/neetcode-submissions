class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev=0
        i=0
        while i < len(nums):
            if i != prev:
                if nums[prev] == nums[i]:
                    return True
                prev += 1
            i += 1
        return False
        
        