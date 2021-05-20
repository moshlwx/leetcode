'''
剑指 Offer 59 - I. 滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/
'''


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        '''
        关键点，减少求最大值时的消耗
        xx 只比较待入队及队首会漏掉队中最大值的情况
        两个思路解决
        1.  借助双向队列，未形成窗口时，遍历num[:i]，将最大值加入队列，
        '''
        # 空值处理
        if not nums or k < 1:
            return []

        import queue
        max_list = []
        max_queue = queue.deque()

        # 前k值，初始化最大值队列
        for i in range(k):
            while max_queue and max_queue[-1] < nums[i]:
                max_queue.pop()
            max_queue.append(nums[i])
        max_list = [max_queue[0]]

        # 形成窗口后
        for i in range(k, len(nums)):
            # 窗口第一位为i-k，若与最大值相同，则排除最大值
            if nums[i-k] == max_queue[0]:
                max_queue.popleft()
            while max_queue and max_queue[-1] < nums[i]:
                max_queue.pop()
            max_queue.append(nums[i])
            max_list.append(max_queue[0])

        return max_list


# 输入：
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# 输出: [3,3,5,5,6,7]
print(Solution().maxSlidingWindow(nums, k))
