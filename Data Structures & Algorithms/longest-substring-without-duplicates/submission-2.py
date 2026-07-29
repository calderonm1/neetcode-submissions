class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        stack = []
        charToIndex = {}

        for i, c in enumerate(s):
            if stack and (charToIndex.get(c) is not None):
                indexToSlice = i - charToIndex[c] - len(stack)

                if indexToSlice <= 0:
                    stack = stack[(abs(indexToSlice) + 1):]
                    print(i, "slicing...")
                
            stack.append(c)
            charToIndex[c] = i

            if len(stack) > maxLength:
                maxLength = len(stack)
                print(i, "new max:", maxLength)
                
            print(i, "stack:", stack)
            print(i, "charToIndex", charToIndex)
            print()

        # abs(index(new) - index(old) - len(stack)) + 1 = index to slice off
        # abs(17 - 4 - 6) + 1 = abs(7) + 1 = 8 (should be invalid)
        # abs(5 - 2 - 3) + 1 = 0 (valid)


        return maxLength
