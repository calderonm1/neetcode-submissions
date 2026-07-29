class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for index, token in enumerate(tokens):
            print(index, "stack:", stack)
            if token in operators:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
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
                stack.append(int(token))

        return stack[-1]


