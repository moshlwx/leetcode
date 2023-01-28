'''
1664. 生成平衡数组的方案数
https://leetcode.cn/problems/ways-to-make-a-fair-array/
给你一个整数数组 nums 。你需要选择 恰好 一个下标（下标从 0 开始）并删除对应的元素。请注意剩下元素的下标可能会因为删除操作而发生改变。

比方说，如果 nums = [6,1,7,4,1] ，那么：

选择删除下标 1 ，剩下的数组为 nums = [6,7,4,1] 。
选择删除下标 2 ，剩下的数组为 nums = [6,1,4,1] 。
选择删除下标 4 ，剩下的数组为 nums = [6,1,7,4] 。
如果一个数组满足奇数下标元素的和与偶数下标元素的和相等，该数组就是一个 平衡数组 。

请你返回删除操作后，剩下的数组 nums 是 平衡数组 的 方案数 。

 

示例 1：

输入：nums = [2,1,6,4]
输出：1
解释：
删除下标 0 ：[1,6,4] -> 偶数元素下标为：1 + 4 = 5 。奇数元素下标为：6 。不平衡。
删除下标 1 ：[2,6,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：6 。平衡。
删除下标 2 ：[2,1,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：1 。不平衡。
删除下标 3 ：[2,1,6] -> 偶数元素下标为：2 + 6 = 8 。奇数元素下标为：1 。不平衡。
只有一种让剩余数组成为平衡数组的方案。
示例 2：

输入：nums = [1,1,1]
输出：3
解释：你可以删除任意元素，剩余数组都是平衡数组。
示例 3：

输入：nums = [1,2,3]
输出：0
解释：不管删除哪个元素，剩下数组都不是平衡数组。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 104
'''


class Solution:

    def waysToMakeFair_baoli(self, nums):
        # 暴力方案，遍历数组，计算剩余元素是否为平衡数组
        def isFair(nums):
            sum_odd = 0
            sum_eve = 0
            for i in range(0, len(nums)):
                if i % 2 == 0:
                    sum_eve += nums[i]
                else:
                    sum_odd += nums[i]
            return sum_eve == sum_odd

        cnt = 0
        for i in range(0, len(nums)):
            if isFair(nums[:i]+nums[i+1:]):
                cnt += 1

        return cnt

    def waysToMakeFair(self, nums):
        # 暴力方案中每次判断是否平衡都是重复计算的，可以考虑利用前缀和等方案预计算结果
        cnt = 0

        pre_sum_odd = [0]*len(nums)
        pre_sum_eve = [nums[0]]*len(nums)
        for i in range(1, len(nums)):
            pre_sum_eve[i] = pre_sum_eve[i-1] \
                + (nums[i] if i % 2 == 0 else 0)
            pre_sum_odd[i] = pre_sum_odd[i-1] \
                + (nums[i] if i % 2 == 1 else 0)

        for i in range(0, len(nums)):
            if pre_sum_eve[i] + pre_sum_odd[-1]-pre_sum_odd[i]  \
                - (nums[i] if i % 2 == 0 else 0)\
                == pre_sum_odd[i] + pre_sum_eve[-1]-pre_sum_eve[i]  \
                    - (nums[i] if i % 2 == 1 else 0):
                cnt += 1

        return cnt


nums = [1, 1, 1]
# ans = 3
print(Solution().waysToMakeFair(nums), Solution().waysToMakeFair_baoli(nums))


nums = [2, 1, 6, 4]
# ans = 1
print(Solution().waysToMakeFair(nums), Solution().waysToMakeFair_baoli(nums))
