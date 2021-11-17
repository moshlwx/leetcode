'''
剑指 Offer II 011. 0 和 1 个数相同的子数组
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

 

示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。
 

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1
 

注意：本题与主站 525 题相同： https://leetcode-cn.com/problems/contiguous-array/
'''


class Solution:
    def findMaxLength(self, nums) -> int:
        '''k-i = 2*(sum[:k] - sum[:i])
        k-2sum[:k] = i - 2sum[:i]
        所以将i-2sum[:i]作为key，val为count，遍历数组，寻找前置子串中符合的个数
        '''
        pre_counter = {}
        pre_counter[0] = 0
        pre_sum = 0
        res = 0

        for i in range(1, len(nums)+1):
            # 推算时数组下标是从1开始的，注意i, n的对应关系
            n = nums[i-1]
            pre_sum += n
            if pre_counter.get(i-2*pre_sum, 'Null') != 'Null':  # 注意get返回0时，if条件不满足
                pre_idx = pre_counter[i-2*pre_sum]
                res = max(res, i-pre_idx)
                # print(i, pre_idx)
            else:
                pre_counter[i-2*pre_sum] = i

        return res


# nums = [1, 0, 1, 1, 0, 1]
# # 输出: 4
# print(Solution().findMaxLength(nums))


nums = [0, 1, 1, 0, 1]
# 输出: 4
print(Solution().findMaxLength(nums))
