'''
剑指 Offer II 012. 左右两边子数组的和相等
给你一个整数数组 nums ，请计算数组的 中心下标 。

数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。

如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。

 

示例 1：

输入：nums = [1,7,3,6,5,6]
输出：3
解释：
中心下标是 3 。
左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。
示例 2：

输入：nums = [1, 2, 3]
输出：-1
解释：
数组中不存在满足此条件的中心下标。
示例 3：

输入：nums = [2, 1, -1]
输出：0
解释：
中心下标是 0 。
左侧数之和 sum = 0 ，（下标 0 左侧不存在元素），
右侧数之和 sum = nums[1] + nums[2] = 1 + -1 = 0 。
 

提示：

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
 

注意：本题与主站 724 题相同： https://leetcode-cn.com/problems/find-pivot-index/

通过次数6,899提交次数10,368
'''


class Solution:
    def pivotIndex(self, nums) -> int:
        '''做sum之后
        遍历元素，计算左右和
        '''

        res = -1
        left = 0
        right = sum(nums)
        pre = 0

        for i, n in enumerate(nums):
            left += pre
            pre = n
            right -= n

            if left == right:
                return i

        return res


# 输入：
nums = [2, 1, -1]
# 输出：3

print(Solution().pivotIndex(nums))
