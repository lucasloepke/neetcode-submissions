class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        snums = []
        for i, j in enumerate(nums):
            snums.append([j,i])
        snums.sort()

        i, j = 0, len(nums)-1

        while i < j:
            if snums[i][0] + snums[j][0] < target:
                i += 1
            elif snums[i][0] + snums[j][0] > target:
                j -= 1
            else:
                break
        submit = [snums[i][1], snums[j][1]]
        return (sorted(submit))