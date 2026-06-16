class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = ["+","-","*","/"]

        stack = []

        for token in tokens:
            if token in operand:
                if stack:
                    print(stack)
                    second = stack.pop()
                    print(second)
                    first = stack.pop()
                    print(first)
                result = eval(str(first) + token + str(second))
                print(result)
                stack.append(int(result))
                print(stack)
                print("-----------")
            else:
                stack.append(token)
        return int(stack[-1])






