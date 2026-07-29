class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = 999

        for price in prices:
            profit = 0
            if price < minPrice:
                minPrice = price
            elif price > minPrice:
                profit = price - minPrice
                maxProfit = max(profit, maxProfit) 

        return maxProfit

            


# 10, 2, 99, 1, 15
# 99 - 2 is correct, not 15 - 1