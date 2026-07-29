class Solution:
    def trap(self, heights: List[int]) -> int:
        water = 0

        for index, height in enumerate(heights):
            leftMax = height
            rightMax = height

            for i in range(0, index):
                if heights[i] > leftMax:
                    leftMax = heights[i]
            
            for i in range(index, len(heights)):
                if heights[i] > rightMax:
                    rightMax = heights[i]

            water += min(leftMax, rightMax) - height

        return water
