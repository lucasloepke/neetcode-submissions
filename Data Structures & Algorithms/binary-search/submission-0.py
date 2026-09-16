class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)-1
        l = 0
        cur = int(len(nums)/2)
        while l < r:
            if nums[cur] < target:
                l = cur+1
            elif nums[cur] > target:
                r = cur-1
            elif nums[cur] == target:
                return cur
            cur = int((r-l)/2 + l)
        if nums[cur] == target:
            return cur
        return -1