from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 : return 0
        res, left, right = 0, 0, 1
        while right < len(prices):
            if prices[right] > prices[left]:
                diff = prices[right] - prices[left]
                res = res if res > diff else diff
            else:
                left = right
            right += 1
        return res
    def rev_maxProfit(self, prices: List[int]) -> int:
        maxV, p_SM = 0, prices[0]
        if len(prices) == 1 :
            return maxV
        for p in prices:
            p_Cur = p
            pft_Cur = p_Cur - p_SM
            if  maxV < pft_Cur :
                maxV = pft_Cur
            if  p_SM > p_Cur :
                p_SM = p_Cur
        return maxV
slt = Solution()    
# Test Case
slt.maxProfit([7,1,5,3,6,4])
#slt.rev_maxProfit([7,2,9,1,5,6,4])
slt.rev_maxProfit([7,8,5,3,6,4])
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
