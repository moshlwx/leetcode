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
        双指针方法，先排序O(n) + O(n^2)
        优化点 判断重复元素直接跳过，现在用set去重，略慢，但是能通过
        '''
        res = []

        nums = sorted(nums)

        for i, ni in enumerate(nums):
            if i > 0 and ni == nums[i-1]:
                continue

            left = i+1  # 从i开始寻找
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] > -ni:
                    right -= 1
                elif nums[left] + nums[right] < -ni:
                    left += 1
                else:
                    if left != i and right != i:
                        res.append([ni, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    # 当出现重复元素时，跳过，注意是在sum==0的条件中跳过，
                    # 在外面循环中跳过会额外跳过没计算过sum的元素
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return res

    def threeSum_Counter(self, nums):
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
nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
# 输出：[[-1,-1,2],[-1,0,1]]
print(Solution().threeSum(nums))
print(Solution().threeSum_Counter(nums))
