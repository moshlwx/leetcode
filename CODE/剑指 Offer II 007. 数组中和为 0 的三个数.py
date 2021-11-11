'''
剑指 Offer II 007. 数组中和为 0 的三个数
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 不重复 的三元组。

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]
 

提示：

0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
 

注意：本题与主站 15 题相同：https://leetcode-cn.com/problems/3sum/
'''


class Solution:
    def threeSum(self, nums):
        '''数组的大小1000，应该接受O(nlogn)~O(n^2)级别的复杂度
        哈希表方法，用暴力O(n) + O(n^2)
        '''
        res = set()
        from collections import Counter

        nums_counter = Counter(nums)
        nums = sorted(nums_counter.elements())

        for i, ni in enumerate(nums):
            for j, nj in enumerate(nums[i+1:]):
                nums_counter[ni] -= 1
                nums_counter[nj] -= 1
                if 0-ni-nj in nums_counter.elements():
                    res.add(tuple(sorted([ni, nj, 0-ni-nj])))
                # else:
                nums_counter[ni] += 1
                nums_counter[nj] += 1

        return [list(i) for i in res]


# 输入：
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
# 输出：[[-1,-1,2],[-1,0,1]]
print(Solution().threeSum(nums))
