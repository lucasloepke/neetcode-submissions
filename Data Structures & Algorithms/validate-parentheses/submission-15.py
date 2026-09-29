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
            elif i in '}])' and stack:
                if keys[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if not stack:
            return True
        else:
            return False