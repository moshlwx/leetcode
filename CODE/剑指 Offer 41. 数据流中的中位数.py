'''
剑指 Offer 41. 数据流中的中位数
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：

输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
 

限制：

最多会对 addNum、findMedian 进行 50000 次调用。
注意：本题与主站 295 题相同：https://leetcode-cn.com/problems/find-median-from-data-stream/
'''
from heapq import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 较大值定义为最小堆
        self.bigger = []
        # 较小的一半定义为最大堆
        self.smaller = []

    def addNum(self, num: int) -> None:
        if len(self.bigger) != len(self.smaller):
            heappush(self.bigger, num)
            # 当为奇数时，将num插入到较大值中，然后左移较大半区的最小值到较小半区
            heappush(self.smaller, -heappop(self.bigger))
        else:
            heappush(self.smaller, -num)
            # 当为偶数时，将num插入到较小值中，然后右移移较小半区的最大值到较大半区
            heappush(self.bigger, -heappop(self.smaller))

    def findMedian(self) -> float:
        return self.bigger[0] if len(self.bigger) != len(self.smaller) else (self.bigger[0] - self.smaller[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
num = 1
obj = MedianFinder()

for i in range(11):
    obj.addNum(i)
    print(obj.findMedian())
