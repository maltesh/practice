class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        for i , v in enumerate(prices[1:]):
            print (i,v)
            sell =v
            if sell > buy:
                profit = max (profit, sell-buy)
            else:
                buy = sell
        return profit


a =Solution()

prices = [7,6,4,3,1]
assert 0 == a.maxProfit(prices)

# prices = [7,1,5,3,6,4]
# assert 5 == a.maxProfit(prices)