'''
494. 目标和
给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。



示例 1：

输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
示例 2：

输入：nums = [1], target = 1
输出：1


提示：

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 100
'''


class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        '''
        DFS全排列，搜索目标值，暴力解法O(2^n)，大用例会超时
        考虑记忆化，减少重复运算 -> 类似场景都可以考虑DP
        '''
        self.res = 0
        # self.res_path = set()
        # self.visited = [0] * 10000

        def dfs(sum_in, i):
            print(sum_in, i)
            if i >= len(nums):
                if sum_in == target:
                    self.res += 1
                return

            for sign in [-1, 1]:
                sum_in += (sign * nums[i])
                dfs(sum_in, i+1)
                sum_in -= (sign * nums[i])

        dfs(0, 0)

        return self.res

    def findTargetSumWays_dp(self, nums, S: int) -> int:
        '''设取＋的集合之和为x，取-的集合之和为y
        x+y = sum(nums)
        x-y = S
        求得'x = (S+sum(nums))/2'
        转换为标准01背包问题
        目标值: 'x = (S+sum(nums))/2'
        dp[i][j]: i个数的组合能到j的方法数
        '''
        #  若目标大于集合总和返回0
        # 用例[1,2,7,9,981] 1000000000
        if S > sum(nums):
            return 0

        # 若为奇数返回0
        if (S+sum(nums)) % 2 == 1:
            return 0

        x = (S+sum(nums))//2

        dp = [0 for _ in range(x+1)]
        # base case，空集合有一种方法满足目标为0
        dp[0] = 1

        for i in range(1, len(nums)+1):
            for j in range(x, nums[i-1]-1, -1):
                # 状态转移方程：放->dp[j-cost_i]种方法+不放->dp[j]种方法
                dp[j] = dp[j] + dp[j - nums[i-1]]

        return dp[-1]
# 示例 1：


# 输入：
nums = [1, 1, 1, 1, 1]
target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 示例 2：
print(Solution().findTargetSumWays(nums, target))

# 输入：
nums = [1]
target = 1
# 输出：1
print(Solution().findTargetSumWays(nums, target))
