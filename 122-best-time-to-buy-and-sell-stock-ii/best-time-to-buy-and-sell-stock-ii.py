class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxx = 0
        prev = float("inf")
        profit = 0


        for price in prices:

            if price> prev:
                profit += price-prev
            
            prev = price

        return profit

        