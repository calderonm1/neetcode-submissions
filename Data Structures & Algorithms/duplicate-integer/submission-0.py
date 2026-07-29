class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {}
        for num in nums:
            if not myDict.get(num):
                myDict[num] = 1
            else:
                return True
        return False

