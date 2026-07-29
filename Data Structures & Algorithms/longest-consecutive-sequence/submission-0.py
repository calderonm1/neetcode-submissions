class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for num in nums:
            if (num - 1) not in nums:
                sequence = 0
                while(num in nums):
                    sequence += 1
                    num += 1
                longest = max(longest, sequence)
        return longest
        
