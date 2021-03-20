'''
剑指 Offer 57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5
'''


class Solution:
    def findContinuousSequence(self, target: int):
        '''滑动窗口
        '''
        left = 1
        right = 1
        window_sum = 0
        res = []

        while right < target:
            c = right
            right += 1

            window_sum += c

            while window_sum > target:
                d = left
                left += 1

                window_sum -= d

            if window_sum == target:
                res.append([i for i in range(left, right)])

        return res

        '''暴力解法
        res = []
        for i in range(1, target):
            for j in range(i, target):
                # sums = sum([i for i in range(i, j+1)])
                sums = (i+j) * (j-i+1) / 2
                if sums == target:
                    res.append([i for i in range(i, j+1)])
                    continue
        return res
        '''


target = 15
print(Solution().findContinuousSequence(target))
