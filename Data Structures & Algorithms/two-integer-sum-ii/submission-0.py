class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = []
        for i, j in enumerate(numbers):
            nums.append([j,i])
        
        l, r = 0, len(nums)-1
        while l < r:
            sum = nums[l][0] + nums[r][0]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [nums[l][1]+1,nums[r][1]+1]
        return []