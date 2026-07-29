class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = [0]
        minPrice = 999

        for index, price in enumerate(prices):
            profit = 0
            if price < minPrice:
                minPrice = price
            elif price > minPrice:
                profit = price - minPrice
                if not stack or profit > stack[-1]:
                    stack.append(profit)


        return stack[-1]

            


# 10, 2, 99, 1, 15
# 99 - 2 is correct, not 15 - 1