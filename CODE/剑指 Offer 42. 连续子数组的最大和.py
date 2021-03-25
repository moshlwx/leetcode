'''
剑指 Offer 42. 连续子数组的最大和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 

提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/
'''


class Solution:
    def maxSubArray(self, nums) -> int:
        '''滑动窗口方法走不通，收缩左边界无法判断，最大子序列为什么不能用滑动窗口呢（有负数）
        动态规划 dp[i]定义为，截止元素为num[i]时的最大连续和
        '''
        dp = [float('-inf')] * (len(nums)+1)
        dp[0] = 0
        res = float('-inf')
        # dp[1] = nums[1]

        for i in range(1, len(nums)+1):
            # dp[i] = max(dp[i-1]+nums[i-1], dp[i-1]) # 不满足连续序列的限制
            # dp[i]定义为，截止元素为num[i]时的最大连续和
            dp[i] = max(nums[i-1], dp[i-1]+nums[i-1])
            res = max(res, dp[i])

        return res


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(Solution().maxSubArray(nums))
