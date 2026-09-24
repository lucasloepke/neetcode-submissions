class Solution:
    def isValid(self, s: str) -> bool:
        keys = {
            '[':']',
            '{':'}',
            '(':')'
        }
        heap = deque()
        for i in s:
            if i in keys:
                heap.append(i)
            elif i in '}])':
                if not heap:
                    return False
                item = heap.pop()
                if keys[item] != i:
                    return False
        return len(heap) == 0


