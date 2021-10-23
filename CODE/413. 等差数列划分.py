'''
413. 等差数列划分
如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。

 

示例 1：

输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
示例 2：

输入：nums = [1]
输出：0
 

提示：

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
'''


class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        # 滑动窗口。
        # 合法性判断
        # - 1. 差值是否变化
        # - 2. 窗口>3

        left = 0
        right = 0
        diff = 0
        vaild_flag = False
        count = 0

        while right < len(nums):
            c = nums[right]
            right += 1

            while not vaild_flag:
                if nums[right] - c == diff and right-left >= 3:
                    vaild_flag = True
                    count += 1
                diff = nums[right] - c

                d = nums[left]
                left += 1

        return count


s = Solution()
nums = [1, 2, 3, 4]
print(s.numberOfArithmeticSlices(nums))
