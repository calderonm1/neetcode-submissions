class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for index, token in enumerate(tokens):
            print(index, "stack:", stack)
            if token in operators:
                operand_1 = int(stack.pop())
                operand_2 = int(stack.pop())
                result = None

                if token == "+":
                    result = operand_1 + operand_2
                elif token == "-":
                    result = operand_1 - operand_2
                elif token == "*":
                    result = operand_1 * operand_2
                else:
                    result = int(operand_1 / operand_2)
                
                stack.append(result)
            else:
                stack.append(token)

        return stack[-1]


