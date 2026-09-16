class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all = 1
        zero = 0
        for i in nums:
            if i != 0:
                all *= i
            else:
                zero += 1

        for i in range(len(nums)):
            if (zero == 0) and (nums[i] != 0):
                nums[i] = int(all / nums[i])
            elif (zero == 1) and (nums[i] == 0):
                nums[i] = all
            else:
                nums[i] = 0

        return nums