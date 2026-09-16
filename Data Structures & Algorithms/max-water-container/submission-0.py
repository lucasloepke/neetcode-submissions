class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front = 0
        end = len(heights)-1
        best = 0
        while front < end:
            calc = (end - front) * min(heights[front], heights[end])
            if calc > best:
                best = calc
            if heights[front] > heights[end]:
                end -= 1
            else:
                front += 1
        return best
