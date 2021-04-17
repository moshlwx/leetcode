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
    def jump(self, nums) -> int:
        '''（未解决）
        贪心算法，坐标起点+步长算出区间
        转换为重叠区间类问题
        '''
        jump_range = []
        jump_cnt = 0
        end = 0
        if nums == [0]:
            return 0
        # 坐标起点+补偿算出区间
        for i, n in enumerate(nums):
            jump_range.append([i, i+n])

        # 按照区间终点排序
        jump_range_sorted = sorted(jump_range, key=lambda x: x[1])
        max_end = jump_range_sorted[0][1]

        for i in jump_range_sorted:
            if i[0] <= max_end:
                max_end = max(max_end, i[1])

            if i[0] == end:
                jump_cnt += 1
                end = max_end

            if max_end >= len(nums)-1:
                return jump_cnt


nums = [1,2,3,4,5]
print(Solution().jump(nums))
