'''
45. 跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。
'''


class Solution:
    def jump_dp(self, nums) -> int:
        '''动态规划思想解决问题
        dp[i]: 第i个位置的最小跳跃数、最远距离
        dp[i] = 若dp[i-1]最远距离>i，则dp[i-1]否则dp[i-1]+1
        '''

        jump_range = []
        # 坐标起点+补偿算出区间
        for i, n in enumerate(nums):
            jump_range.append([i, i+n])
        jump_range_sorted = sorted(jump_range, key=lambda x: x[1])

        dp = [[0, 0] for _ in range(len(nums)+1)]

        for i in range(len(nums)+1):
            dp[i][0] = dp[i-1][0] + (dp[i-1][1] > i)
            dp[i][1] = max(dp[i-1][1], jump_range_sorted[i])

        return dp[-1][0]

    def jump(self, nums) -> int:
        '''
        贪心算法
        '''
        jump_cnt = 0
        end = 0
        max_end = 0

        # 这里循环到len(nums)-2提前结束，可以减少当前覆盖最远距离下标是否终点的判断
        # 详细解析：https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0045.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8FII.md
        for i in range(len(nums)-1):
            max_end = max(max_end, i+nums[i])

            if i == end:
                jump_cnt += 1
                end = max_end

        return jump_cnt


nums = [2, 3, 1, 1, 4]
print(Solution().jump(nums))

# assert Solution().jump([1, 2, 3, 4, 5]) == 3
# assert Solution().jump([2, 3, 1, 1, 4]) == 2
# assert Solution().jump([2, 3, 0, 1, 4]) == 2
