class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            if not num in res:
                res[num] = 0
            res[num] += 1
        
        ans = [0] * k
        for i in range(k):
            max_val = 0
            max_key = 0
            for key in res:
                if res[key] > max_val:
                    max_val = res[key]
                    max_key = key
            ans[i] = max_key
            res[max_key] = -1
        
        return ans

