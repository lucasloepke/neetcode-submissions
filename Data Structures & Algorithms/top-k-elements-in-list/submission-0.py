class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_arr = sorted(nums, key=Counter(nums).get, reverse=True)
        unique_array = list(dict.fromkeys(sorted_arr))
        return unique_array[0:k]