class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
            We solve the problem in one pass through the array.

            1. Maintain `lowest_buy_price` to track the minimum price seen so far.
            2. For each price:
            - Calculate the potential profit (`price - lowest_buy_price`) and update `profit` 
            if it's higher.
            - Update `lowest_buy_price` if the current price is lower.

            Time Complexity: O(n) - We traverse the prices once.
            Space Complexity: O(1) - Only two variables are used to store state.
        """
        if len(prices) < 2:
            return 0
        
        lowest_buy_price = prices[0]
        profit = 0

        for price in prices[1:]:
            if price - lowest_buy_price > profit:
                profit =  price - lowest_buy_price
            if price < lowest_buy_price:
                lowest_buy_price = price

        return profit
