from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy when slop is low 
        # sell when slop is high 
        if len(prices) == 1:
            return 0
        max_profit = 0
        buy, sell = 0, 1
        while sell < len(prices):
            # profit 
            if prices[sell]  - prices[buy] <= 0:
                buy = sell
            else:
                max_profit = max(prices[sell]  - prices[buy], max_profit)
            sell += 1
        return max_profit
if __name__ == "__main__":

    '''
        Expected - 
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    '''
    obj = Solution()
    prices = [7,1,5,3,6,4]
    res = obj.maxProfit(prices)
    print(res)