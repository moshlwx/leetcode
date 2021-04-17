'''
55. 跳跃游戏
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

 

示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
 

提示：

1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105
'''


class Solution:
    def canJump(self, nums) -> bool:
        '''
        贪心算法，坐标起点+步长算出区间
        转换为重叠区间类问题
        '''
        jump_range = []
        # 坐标起点+补偿算出区间
        for i, n in enumerate(nums):
            jump_range.append([i, i+n])

        # 按照区间终点排序
        jump_range_sorted = sorted(jump_range, key=lambda x: x[1])
        max_end = jump_range_sorted[0][1]

        for i in jump_range_sorted:
            if i[0] <= max_end:
                max_end = max(max_end, i[1])

            if max_end >= len(nums)-1:
                return True

        return False


nums = [0]
print(Solution().canJump(nums))
