class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy,sell = 0,1 #Two pointers starting at 0,1
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit,profit)
            else:
                buy = sell
            sell += 1   
        return maxProfit