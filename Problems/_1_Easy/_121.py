from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        if prices == sorted(prices, reverse=True):
            return 0
        maxList = {}
        for idx, p in enumerate(prices):
            cur = p
            ava_list = list(map(lambda x: x - cur, prices[idx+1 : len(prices)]))
            v_max = 0 if len(ava_list) == 0 else max(ava_list)
            if v_max > 0 and v_max not in maxList  :
                maxList[v_max] = v_max
            #arr = list(map(lambda x: x - cur, prices[idx+1 : len(prices)-1]))
        r = max(maxList, key=maxList.get)
        print(r)
        return r
    
    def rev_maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1 :
            return 0

        smallestSoFar = prices[0]
        maxValue = prices[1] - prices[0]
        for idx in range(1,len(prices)):
            if idx == len(prices)-1:
                break
            cur = prices[idx]
            smallestSoFar = min(smallestSoFar, cur)
            nxt = prices[idx+1]

            substract = nxt - smallestSoFar
            if substract > maxValue:
                maxValue = substract 
        return maxValue if maxValue > 0 else 0
        return maxValue
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
