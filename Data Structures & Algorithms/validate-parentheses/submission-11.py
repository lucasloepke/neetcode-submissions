class Solution:
    def isValid(self, s: str) -> bool:
        keys = {
            '[':']',
            '{':'}',
            '(':')'
        }
        heap = []

        for i in s:
            if i in '({[':
                heap.append(i)
            elif i in '}])':
                if heap and (i == keys[heap[-1]]):
                    heap.pop()
                else:
                    return False

        if not heap:
            return True
        else:
            return False