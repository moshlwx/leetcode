'''
剑指 Offer 61. 扑克牌中的顺子
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

 

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True
 

限制：

数组长度为 5 

数组的数取值为 [0, 13] .
'''

class Solution:

    def isStraight(self, nums) -> bool:
        '''
        1. 数组中元素除大小王无重复 set
        2. 最大值-最小值小于等于4
        '''
        visited = set()
        max_val = float('-inf')
        min_val = float('inf')

        for n in nums:
            if n == 0:
                continue
            max_val = max(max_val, n)
            min_val = min(min_val, n)
            if n in visited or max_val - min_val >= 5:
                return False
            visited.add(n)
        
        return True
        


    def isStraight_指针(self, nums) -> bool:
        '''判断一串数字是否连续序，同时0可以为滑动窗口
        '''
        # 先排序
        nums.sort()
        cur = 0
        lmt = 1

        while nums[cur] == 0:
            cur += 1
            lmt += 1
        
        pre = nums[cur] - 1

        while cur < len(nums):
            if nums[cur] - pre <= lmt and nums[cur] - pre != 0:
                lmt -= (nums[cur] - pre - 1)
            else:
                return False
            
            pre = nums[cur]
            cur += 1
        return True

nums = [0, 0, 6, 7, 5]
print(Solution().isStraight(nums))
