class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l = r = 0
        q = collections.deque()

        while r < len(nums):
            # deque must be in monotonically decreasing order (ex. 7, 4, 3, 1...)
            while q and nums[r] > nums[q[-1]]:
                q.pop()

            # append here to prevent extra check on q below 
            q.append(r)

            # if first element in deque is outside of window, it must be popped
            if q[0] < l:
                q.popleft()

            # ensure the window is valid
            while (r + 1) - l >= k:
                l += 1
                result.append(nums[q[0]])

            r += 1
            
        return result

            
            
        




