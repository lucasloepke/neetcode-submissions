class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        nums.sort()
        # [-4,-1,-1,0,1,2]
        final = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i+1, len(nums)-1
            while j < k:
                localsum = nums[i] + nums[j] + nums[k]
                if localsum < 0:
                    j += 1
                elif localsum > 0:
                    k -= 1
                else:
                    final.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -=1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return final