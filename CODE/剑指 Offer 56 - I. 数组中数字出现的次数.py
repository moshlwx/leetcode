'''
剑指 Offer 56 - I. 数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 

限制：

2 <= nums.length <= 10000
 
'''


class Solution:
    def singleNumbersCounter(self, nums):
        from collections import Counter
        cnt = Counter(nums)
        res = []

        for i in cnt:
            if cnt[i] == 1:
                res.append(i)
        return res

    def singleNumbers(self, nums):
        '''集合做异或（若不同则为原值，相同则为0），仅出现一次的元素保留
        i ^ j 指i的二进制按位异或j的二进制，若不同则1，若相同则0
        '''
        res = 0
        div = 1
        a = 0
        b = 0

        for n in nums:
            res ^= n

        # res中任选一个位置为1的二进制数div
        while div & res == 0:
            # div找到第一个res中1的位置
            div <<= 1
        # 将数组分为两组，第i位与div相同与不同的分别到不同组
        for n in nums:
            if (n & div) == 0: # python操作符优先级&》==，所以不用加括号，C中需要加，默认都加着
                a ^= n
            else:
                b ^= n

        return [a, b]


nums = [1, 2, 10, 4, 1, 4, 3, 3]
print(Solution().singleNumbers(nums))
