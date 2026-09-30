class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isnumeric():
                stack.append(int(i))
            elif i[0] == '-' and len(i) > 1:
                stack.append(-1*int(i[1:]))
            else:
                if i == "+":
                    val = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                elif i == "-":
                    val = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                elif i == "*":
                    val = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                elif i == "/":
                    val = int(stack[-2] / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(val)

        return stack[-1]
                 