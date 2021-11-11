'''
剑指 Offer II 004. 只出现一次的数字
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。



示例 1：

输入：nums = [2,2,3,2]
输出：3
示例 2：

输入：nums = [0,1,0,1,0,1,100]
输出：100


提示：

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次


进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？



注意：本题与主站 137 题相同：https://leetcode-cn.com/problems/single-number-ii/
'''


class Solution:
    def singleNumber(self, nums) -> int:
        '''位运算，32位的二进制数字，每个位上面总和求余3，最后的结果就是只出现一次的数字
        时间O(n)
        空间O(1)
        int('0b'+''.join(a[::-1]), 2)
        '''
        res = 0
        a = 0
        for i in range(32):
            # 按位加总 
            # (n >> i) & 1 取n的二进制第i位
            if sum([(n >> i) & 1 for n in nums]) % 3:
                if i == 31: 
                    # python 无符号整数，最高位为1时，是负数
                    a -= (1 << i)
                else:
                    # 若第i位求余3有内容，则结果的二进制第i位置1
                    a |= (1 << i)

        return a

    def singleNumber_sliding_window(self, nums) -> int:
        '''滑动窗口，当窗口内只含出现一次时右移，否则左移
        时间O(n)
        空间O(1)，存储左右指针
        '''
        from collections import Counter
        nums_set = Counter(nums)
        for k, v in nums_set.items():
            if v == 1:
                return k

    def singleNumber_counter(self, nums) -> int:
        '''计数，返回count=1的key
        时间O(n)+O(n)
        空间O(n/3)
        '''
        from collections import Counter
        nums_set = Counter(nums)
        for k, v in nums_set.items():
            if v == 1:
                return k


# 输入：
nums = [0, 1, 0, 1, 0, 1, 100]
# 输出：100
print(Solution().singleNumber(nums))
