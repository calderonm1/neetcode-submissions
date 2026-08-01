class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use floyds algorithm to find the beginning of a cycle in a linkedin
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            # eventually, fast and slow will point to the same node
            if fast == slow: break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2: break
        
        return slow