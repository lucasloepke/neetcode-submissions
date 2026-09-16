class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        A = sorted(nums)
        prev = 0
        i = 1

        while i < (len(A)):
            if A[i] == A[prev]:
                return True
            i += 1
            prev += 1
        return False