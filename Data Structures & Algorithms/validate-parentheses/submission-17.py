class Solution:
    def isValid(self, s: str) -> bool:
        keys = {
            '{':'}',
            '(':')',
            '[':']'
        }

        stack = deque()

        for i in s:
            if i in '{[(':
                stack.append(i)
            elif i in '}])' and stack and keys[stack[-1]] == i:
                stack.pop()
            else:
                return False
        return not stack