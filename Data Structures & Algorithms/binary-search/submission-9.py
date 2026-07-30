class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_bound = 0
        upper_bound = len(nums) - 1

        while True:
            i = math.floor((lower_bound + upper_bound)/2)
            if nums[i] == target:
                return i
            if lower_bound == upper_bound:
                return -1
            if nums[i] < target:
                upper_bound = i
            if nums[i] > target:
                lower_bound = i