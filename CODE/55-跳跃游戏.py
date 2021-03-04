'''
55. 跳跃游戏
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

 

示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
 

提示：

1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105
'''
class Solution:
    def canJump(self, nums) -> bool:
        '''
        dp[i] 第i个位置能否到达
        状态转移
        dp[i] = dp[i-k] and nums(i-k)>k
        '''
        if nums == [0]:
            return True

        dp = [False for _ in range(len(nums)+1)]
        dp[0] = True

        for i in range(1, len(nums)+1):
            for k in range(i, 0, -1):
                # 边界存在问题，包括k的循环范围及nums的判断
                dp[i] = dp[i] or (dp[i-k] and (nums[i-k]>=k-1))
        
        return dp[-1]

nums = [2, 0, 0]
print(Solution().canJump(nums))