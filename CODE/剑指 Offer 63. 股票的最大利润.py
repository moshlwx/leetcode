'''剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 

限制：

0 <= 数组长度 <= 10^5

 

注意：本题与主站 121 题相同：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
'''


class Solution:
    def maxProfit(self, prices) -> int:
        '''遍历prices，保存历史中最低价，计算最大差额
        '''
        # left = 0
        right = 0
        max_diff = 0
        min_prices = float('inf')

        while right < len(prices):
            min_prices = min(prices[right], min_prices)
            max_diff = max(max_diff, prices[right] - min_prices)

            right += 1

        return max_diff

    def maxProfit_dp(self, prices) -> int:
        '''第二天开始计算当日盈亏，转换为动态规划问题计算最大子序列和
        dp[i] 第i天的最大利润
        dp[i] = max(dp[i-1]+diff[i-1], diff[i-1])
        '''
        # 可以合并到循环计算中，减少一次对prices的遍历
        diff = [prices[i]-prices[i-1] for i in range(1, len(prices))]
        res = 0

        dp = [float('-inf')] * (len(diff)+1)
        dp[0] = 0

        for i in range(1, len(diff)+1):
            dp[i] = max(dp[i-1]+diff[i-1], diff[i-1])
            res = max(res, dp[i])

        return res


# 输入: [7,1,5,3,6,4]
prices = [7, 1, 5, 3, 6, 4]
# 输出: 5
print(Solution().maxProfit(prices))
