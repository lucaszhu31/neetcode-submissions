class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0

        for i in range(len(prices)-1):
            if prices[i+1] < min:
                min = prices[i+1]
            elif prices[i+1] - min > profit:
                profit = prices[i+1] - min 
        
        return profit
        