class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }

        for c in s:
            if c in brackets:
                stack.append(brackets.get(c))

            elif (len(stack) > 0 and c == stack[-1]):
                stack.pop()

            else:
                return False
        return True