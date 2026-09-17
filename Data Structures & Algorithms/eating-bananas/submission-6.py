class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r

        while l <= r:
            m = (r + l) // 2
            hours = 0

            # determine the amount of time to eat all of the bananas
            # print("k:", k, "| l:", l, "| r:", r)
            for pile in piles:
                # print("it took", -(-pile // m), "hours to eat", pile, "bananas at rate", m)
                hours += -(-pile // m)
                
            # print("total hours to eat bananas at rate", m, "is", hours)

            if hours <= h:
                k = m
                r = m - 1
            else:
                l = m + 1

            # print()

        return k