class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort the array
        for i in range(1, len(nums)):
            for j in range(0, len(nums) - 1):
                if (nums[j] > nums[i]):
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
        print(nums)

        # two sum looking for compliment
        for idx, target in enumerate(nums):
            lp = idx + 1
            rp = len(nums) - 1

            while (lp < rp):
                if nums[lp] + nums[rp] == -target:
                    res.append([nums[lp],nums[rp],target])
                    break
                if nums[lp] + nums[rp] > -target:
                    rp -= 1
                    continue
                lp += 1

        return res

            

