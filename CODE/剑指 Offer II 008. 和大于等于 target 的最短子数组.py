'''
剑指 Offer II 008. 和大于等于 target 的最短子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
 

提示：

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
 

进阶：

如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
 

注意：本题与主站 209 题相同：https://leetcode-cn.com/problems/minimum-size-subarray-sum/
'''


class Solution:

    def minSubArrayLen(self, target: int, nums) -> int:
        '''前缀和+二分查找，元素均为正数，前缀和递增，可以用二分查找定位
        O(nlog(n))
        '''
        res = float('inf')
        window_sum = 0
        # 每次sum可能会慢，可以用递增tmp变量
        nums_sum = [sum(nums[:i]) for i in range(len(nums))]
        import bisect

        for i, n in enumerate(nums):
            window_sum += n
            left = bisect.bisect_left(nums_sum, target-window_sum)
            res = min(res, left-i)

        return res if res != float('inf') else 0

    def minSubArrayLen_window(self, target: int, nums) -> int:
        '''滑动窗口
        窗口内和大于target left+= 1，和小于target righ+=1
        O(n)
        '''
        res = float('inf')
        window_sum = 0

        left = 0
        right = 0

        while right < len(nums):
            c = nums[right]
            window_sum += c
            right += 1

            while window_sum >= target:
                res = min(res, right-left)
                d = nums[left]
                left += 1
                window_sum -= d

        return res if res != float('inf') else 0


# 输入：
target = 7
nums = [2, 3, 1, 2, 4, 3]
# 输出：0
print(Solution().minSubArrayLen(target, nums))
