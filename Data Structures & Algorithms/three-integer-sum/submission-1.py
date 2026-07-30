class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort

        # two sum looking for compliment
        for i, a in enumerate(nums):
            if (a == nums[i-1]):
                continue
            lp = i + 1
            rp = len(nums) - 1
            compliment = -a

            while (lp < rp):
                if nums[lp] + nums[rp] == compliment:
                    res.append([nums[lp],nums[rp],target])
                    break
                if nums[lp] + nums[rp] > compliment:
                    rp -= 1
                    continue
                lp += 1

        return res

            

