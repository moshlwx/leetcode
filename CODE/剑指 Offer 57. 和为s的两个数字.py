'''
剑指 Offer 57. 和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
 

限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
'''


import math
from time import perf_counter


class Solution:
    def twoSum(self, nums, target: int):
        '''双指针方法，利用有序特性，分别从前后扫描
        '''
        left = 0
        right = len(nums)-1

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] == target:
                return [nums[left], nums[right]]

        return []

    def twoSum_hash(self, nums, target: int):
        '''利用哈希表复杂度O(n)空间复杂度O(n)
        '''
        num_tar = {target - i for i in nums}

        for n in nums:
            if n in num_tar:
                return [n, target-n]
        return []

    def twoSum_bin(self, nums, target: int):
        '''二分查找解法，复杂度O(nlogn)会超时
        '''
        self.cnt = 0
        for i in range(len(nums)):
            res_target = target - nums[i]

            if self.find_target(res_target, nums[i+1:]):
                print(self.cnt)
                return [nums[i], res_target]
        print(self.cnt)
        return []

    def find_target(self, target, nums):
        '''有序数组中找target，考虑用二分查找
        存在返回真，否则为假
        '''
        low = 0
        high = len(nums)-1 # 注意-1

        while low <= high:
            self.cnt += 1
            mid = (low + high) // 2

            if target > nums[mid]:
                low = mid+1 # 需要迭代+1
            elif target < nums[mid]:
                high = mid-1 # 需要迭代-1
            else:
                # target == nums[mid]
                return True

        return False


# 输入：
nums = [i*2+100 for i in range(10**5)]
target = 4000
start = perf_counter()
print(Solution().twoSum(nums, target))
print('复杂度： ', round(len(nums)*math.log2(len(nums))))
# 10^6数据量，O(nlogn)复杂度也会超时
print(perf_counter() - start)
