class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = ["+","-","*","/"]
        stack = []

        for token in tokens:
            if token in operand:
                if stack:
                    second = stack.pop()
                    first = stack.pop()
                result = eval(str(first) + token + str(second))
                stack.append(int(result))
            else:
                stack.append(token)
        return int(stack[0])






