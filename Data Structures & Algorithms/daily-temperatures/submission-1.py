class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            c = 1
            while stack and t > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
                c += 1

            stack.append(i)

        return result
