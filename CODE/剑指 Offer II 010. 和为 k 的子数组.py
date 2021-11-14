'''
剑指 Offer II 010. 和为 k 的子数组
给定一个整数数组和一个整数 k ，请找到该数组中和为 k 的连续子数组的个数。

 

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2
解释: 此题 [1,1] 与 [1,1] 为两种不同的情况
示例 2 :

输入:nums = [1,2,3], k = 3
输出: 2
 

提示:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

 

注意：本题与主站 560 题相同： https://leetcode-cn.com/problems/subarray-sum-equals-k/

通过次数7,449提交次数16,874
'''


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        '''滑动窗口，有负数，不好判断窗口收缩或扩展
        前缀和+二分查找，有负数，前缀和也不能保证递增，二分查找不好用
        '''

        '''
        res = 0
        left = 0
        right = 0
        window_sum = 0

        while right < len(nums):
            c = nums[right]
            right += 1
            window_sum += c

            while window_sum == k:
                print(nums[left: right])
                res += 1
                d = nums[left]
                left += 1
                window_sum -= d

        return res
        '''
        from collections import Counter
        res = 0
        nums_sum = Counter(sum(nums[:i+1]) for i in range(len(nums)))

        for i, n in enumerate(nums):
            if k-n in nums_sum.elements():
                res += nums_sum.get(k-n)
        return res


# 输入:
nums = [1, 2, 3]
k = 3
# 输出: 2
print(Solution().subarraySum(nums, k))
