'''
剑指 Offer II 009. 乘积小于 K 的子数组
给定一个正整数数组 nums和整数 k ，请找出该数组内乘积小于 k 的连续的子数组的个数。

 

示例 1:

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8 个乘积小于 100 的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
示例 2:

输入: nums = [1,2,3], k = 0
输出: 0
 

提示: 

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
 

注意：本题与主站 713 题相同：https://leetcode-cn.com/problems/subarray-product-less-than-k/ 
'''


class Solution:

    def numSubarrayProductLessThanK_bisect(self, nums, k: int) -> int:
        '''思路同和大约等于target的最短子数组
        1. 滑动窗口遍历所有子数组组合，O(n)--要求小于，不好求
        2. 前缀乘积+二分查找除数O(nlog(n))
        '''
        import bisect
        res = 0
        nums_prod = []
        tmp = 1
        for n in nums:
            tmp *= n
            nums_prod.append(tmp)

        for i, n in enumerate(nums):
            if bisect.bisect(nums_prod[i]/n):
                res += 1

        return res

    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        '''思路同和大约等于target的最短子数组
        1. 滑动窗口遍历所有子数组组合，O(n)--要求小于，窗口的子数组都可以
        2. 前缀乘积+二分查找除数O(nlog(n))
        '''
        if k < 1:
            return 0

        res = 0
        window_prod = 1

        left = 0
        right = 0

        while right < len(nums):
            c = nums[right]
            right += 1
            window_prod *= c

            # 滑动窗口
            while window_prod >= k and left < right:
                d = nums[left]
                left += 1
                window_prod /= d

            print(nums[left:right])
            res += (right - left) # 每次新的最大窗口会包含right - left个**新的**子数组
        return res


# 输入:
nums =  [10,500,200,6]

k = 100
# 输出: 8
print(Solution().numSubarrayProductLessThanK_sliding_window(nums, k))
