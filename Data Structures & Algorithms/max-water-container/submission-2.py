class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        
        for lp in range(len(heights)):
            rp = lp + 1
            while rp < len(heights):
                area = min(heights[lp], heights[rp]) * (rp - lp)
                maxArea = max(maxArea, area)
                rp += 1
        return maxArea
