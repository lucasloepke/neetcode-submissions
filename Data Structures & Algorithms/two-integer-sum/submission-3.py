class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, j in enumerate(nums):
            A.append([j,i])

        A.sort()
        i=0
        j=len(nums)-1

        while i < j:
            sum = A[i][0] + A[j][0]
            if sum == target:
                x = [A[i][1],A[j][1]]
                x.sort()
                return x
            elif sum > target:
                j -= 1
            elif sum < target:
                i += 1
        return []