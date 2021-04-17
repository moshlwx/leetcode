'''
435. 无重叠区间
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
'''


class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        '''贪心算法
        '''

        # 按照结束区间倒序
        intervals_sorted = sorted(intervals, key=(lambda x: x[1]))
        intervals_min = []
        last_end = float('-inf')

        # 选择最早结束的区间，删除所有相交的区间
        for i in intervals_sorted:
            if i[0] >= last_end:
                intervals_min.append(i)
                last_end = i[1]

        # 得到最大不相交区间个数，总区间树-最大不相交区间个数=最小移除数量
        return len(intervals) - len(intervals_min)


intervals =  [ [1,2], [2,3], [3,4], [1,3] ]

print(Solution().eraseOverlapIntervals(intervals))
