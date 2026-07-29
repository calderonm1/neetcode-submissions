class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # _ 1 2 4 6 _
        # _ 1 2 8 48 _
        # _ 48 48 24 6 _
        # _ 

        # prefix
        prefix = [1] * len(nums)
        for i in range(len(nums)):
            prev = 1
            if i - 1 >= 0:
                prev = prefix[i - 1]
            prefix[i] = prev * nums[i]

        # postfix
        postfix = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            nxt = 1
            if i + 1 < len(nums):
                nxt = postfix[i + 1]
            postfix[i] = nxt * nums[i]
        
        # result
        res = [0] * len(nums)
        for i in range(len(nums)):
            pre = 1
            if i - 1 >= 0:
                pre = prefix[i - 1]

            post = 1
            if i + 1 < len(nums):
                post = postfix[i + 1]
            res[i] = pre * post
        
        return res
