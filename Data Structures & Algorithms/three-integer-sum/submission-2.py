class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)

        # two sum looking for compliment
        for i, a in enumerate(nums):
            lp = i + 1
            rp = len(nums) - 1

            while (lp < rp):
                # triplet found
                if nums[lp] + nums[rp] + a == 0:
                    res.append([nums[lp],nums[rp],a])
                    break
                # sum is greater than compliment
                if nums[lp] + nums[rp] + a > 0:
                    rp -= 1
                    continue
                # sum is less than compliment
                lp += 1
        return res