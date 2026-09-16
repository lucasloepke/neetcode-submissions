class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for x in s:
            if x in '([{':
                stack.append(x)
            elif x == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif x == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif x == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        return not stack