'''
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2
 

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        '''dp[i]总金额i时，最少硬币数
        dp[i] = min([dp[i-c] + c for c in coins])
        '''

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)

        return -1 if dp[-1] == float('inf') else dp[-1]


# 输入：
coins = [1, 2, 5]
amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
print(Solution().coinChange(coins, amount))

coins = [2]
amount = 3
# 输出：- 1
print(Solution().coinChange(coins, amount))


# 输入：
coins = [1]
amount = 0
# 输出：0
print(Solution().coinChange(coins, amount))

# 输入：
coins = [1]
amount = 1
# 输出：1
print(Solution().coinChange(coins, amount))

# 输入：
coins = [1]
amount = 2
print(Solution().coinChange(coins, amount))

# 输入：
coins = [12435]
amount = 2
print(Solution().coinChange(coins, amount))
