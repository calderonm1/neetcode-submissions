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

            elif (c == stack[-1]):
                stack.pop()

            else:
                return False
        return True