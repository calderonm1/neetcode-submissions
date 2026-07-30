class Solution:
    def search(self, nums: List[int], target: int) -> int:
        while (True):
            i = math.floor(len(nums)/2)

            if nums[i] == target:
                return i
            elif len(nums) == 1:
                return -1
            elif nums[i] > target:
                nums = nums[i:len(nums)+1]
            elif nums[i] < target:
                nums = nums[0:i]