class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] < nums[r]:
                if target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[l] <= target:
                    r = r - 1
                else:
                    l = l + 1

        return -1
        
        # target: 3
        # 3 5 1
        # l m r
