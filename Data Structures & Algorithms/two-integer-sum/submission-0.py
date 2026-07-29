class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in myDict:
                difference = target - num
                myDict[difference] = i
                continue
            return [myDict[num], i]
            
        
            
            
            