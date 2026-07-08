class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        sell=0
        profit=0
        max_profit=0
        for i in range(len(prices)):
            if prices[i]<=buy and i!=len(prices)-1:
                buy=prices[i]
                sell=max(prices[i+1:len(prices)])
                profit=sell-buy
            if profit>max_profit:
                max_profit=profit
        return max_profit
        

            

        