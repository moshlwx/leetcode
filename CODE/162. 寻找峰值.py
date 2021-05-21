'''
162. 寻找峰值
峰值元素是指其值大于左右相邻值的元素。

给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

 

示例 1：

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
示例 2：

输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5 
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
 

提示：

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
对于所有有效的 i 都有 nums[i] != nums[i + 1]
 

进阶：你可以实现时间复杂度为 O(logN) 的解决方案吗？
'''


class Solution:
    def findPeakElement(self, nums) -> int:
        '''寻找左边界，左右寻找方向根据上下坡确定
        '''
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # 上坡，则峰顶在右侧
            # 增加mid寻找到边界的判断，若到边界则收缩右边界
            if mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                left = mid + 1
            # 下坡或平坡，则峰顶在左侧
            # elif nums[mid] > nums[mid+1]:
            #     right = mid - 1
            else:
                right = mid - 1

        return left


# 输入：
nums = [1, 2, 1, 3, 5, 6, 4]
# 输出：1 或 5
# 解释：你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
print(Solution().findPeakElement(nums))

nums = [1, 2]
print(Solution().findPeakElement(nums))
