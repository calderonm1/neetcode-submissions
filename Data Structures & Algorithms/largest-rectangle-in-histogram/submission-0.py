class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # stores (startIndex, height) pairs
        maxArea = 0
        
        for i, h in enumerate(heights):
            prev_i = i
            while stack and h < stack[-1][1]:
                height = stack[-1][1]
                width = i - stack[-1][0]
                maxArea = max(maxArea, height * width)
                prev_i = stack[-1][0]
                stack.pop()
            if not stack or stack[-1][1] != h:
                stack.append([min(i, prev_i), h])
        
        while stack:
            height = stack[-1][1]
            width = len(heights) - stack[-1][0]
            maxArea = max(maxArea, height * width)
            stack.pop()
                
        return maxArea
        

