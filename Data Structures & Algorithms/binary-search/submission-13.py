class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_bound = 0
        upper_bound = len(nums) - 1

        while lower_bound <= upper_bound:
            i = math.floor((lower_bound + upper_bound)/2)
            if nums[i] == target:
                return i
            if nums[i] > target:
                upper_bound = i - 1
            if nums[i] < target:
                lower_bound = i + 1
        return -1