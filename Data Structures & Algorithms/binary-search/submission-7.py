class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        cur = r // 2
        while l < r:
            if nums[cur] < target:
                l = cur+1
            elif nums[cur] > target:
                r = cur-1
            elif nums[cur] == target:
                return cur
            cur = (r+l) // 2
        if nums and nums[cur] == target:
            return cur
        return -1