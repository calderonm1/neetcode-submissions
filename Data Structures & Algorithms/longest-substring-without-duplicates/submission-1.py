class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        stack = []
        charToIndex = {}

        for i, c in enumerate(s):
            if stack and (charToIndex.get(c) is not None):
                indexToSlice = abs(i - charToIndex[c] - len(stack)) + 1
                stack = stack[indexToSlice:]
                
            stack.append(c)
            charToIndex[c] = i

            if len(stack) > maxLength:
                maxLength = len(stack)

        return maxLength

    # maxLength = 3
    # a b c a b c b b
    # a b c 
    # 0 1 2

    # index(old) = 2
    # index(new) = 5
    # len(stack) = 3
    # abs|index(new) - index(old) - len(stack)| = index to slice off
    # 6 - 4 - 3 = 1

