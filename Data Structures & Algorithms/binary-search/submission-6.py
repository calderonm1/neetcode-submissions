class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = math.floor((len(nums)-1)/2)
        prev_i = -1

        while (True):
            if nums[i] == target:
                return i

            if i == prev_i:
                return -1

            prev_i = i

            if nums[i] > target:
                i = math.floor(i/2)

            if nums[i] < target:
                i = math.floor((len(nums)+i)/2)