class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        # append a dummy 0 to force clearing the stack at the end
        heights.append(0) 
        
        for i, h in enumerate(heights):
            prev_i = i
            while stack and h < stack[-1][1]:
                popped_i, popped_h = stack.pop() 
                
                width = i - popped_i
                maxArea = max(maxArea, popped_h * width)
                
                # the current rectangle can start at least as far back as the one we just popped
                prev_i = popped_i 
            
            # use a tuple instead of a list
            if not stack or stack[-1][1] != h:
                stack.append((prev_i, h))
                
        return maxArea
