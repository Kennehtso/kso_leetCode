from typing import List
class Solution:
     def maxProfit(self, prices: List[int]) -> int:
        p_smallest, pft_max = prices[0], 0
        for i in range(1,len(prices)):
            p_cur = prices[i]
            #Get the price_current minus smallest price during this time
            pft_cur = p_cur - p_smallest

            # if the currnet prodit is larger, replace it as max profit
            if pft_cur > pft_max:
                pft_max = pft_cur
            # if the current price is lower than smallest price, replace it
            # *** Notice that the index of upcoming price are behind of current price ***
            if p_cur < p_smallest : 
                p_smallest = p_cur
        return pft_max
slt = Solution()
# Test Case
slt.maxProfit([7,99,2,9,1,5,6,4])
slt.maxProfit([7,6,4,3,1])
"""
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the i^th day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
================================================================================================================
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
================================================================================================================

Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 104

"""
