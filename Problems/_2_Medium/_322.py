from typing import List
class Solution:
    # DP - bottom-up
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Use DP bottom up
        # start from 0
        ans = 0
        # initialize all layer with the max amount
        # don't forget the 0, 
        nums = amount + 1
        dp = [nums] * (nums)
        dp[0] = 0
        #print("dp: ",dp)
        for i in range(1, nums):
            #print("%s with %s:"%(i, coins))
            for c in coins:
                diff = i - c
                # decrease the combination of dp[i] 
                if diff >= 0: #include 0
                    dp[i] = min(dp[i], 1 + dp[diff])
                    #print("dp[i] reduce :", dp[i])
            #print("dp: ",dp)
        print(dp)
        return dp[amount] if dp[amount] != nums else -1
        
slt = Solution() 
# Test Case
slt.coinChange([1,3,4,7], 88)
"""
322. Coin Change

You are given an integer array coins representing coins of
different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that 
amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

Example 2:
    Input: coins = [2], amount = 3
    Output: -1

Example 3:
    Input: coins = [1], amount = 0
    Output: 0

Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104

"""