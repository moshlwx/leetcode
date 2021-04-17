[toc]
# 数据结构
## 栈
### 题目
- [剑指 Offer 31. 栈的压入、弹出序列](CODE/剑指%20Offer%2031.%20栈的压入、弹出序列.py)

## 二叉树
二叉树大部分涉及递归思想
### 题目
- [剑指 Offer 28. 对称的二叉树](CODE/剑指%20Offer%2028.%20对称的二叉树.py)
- [236. 二叉树的最近公共祖先](CODE/236-二叉树的最近公共祖先.py)
- [105. 从前序与中序遍历序列构造二叉树](CODE/105-从前序与中序遍历序列构造二叉树.py)
- [剑指 Offer 55 - I. 二叉树的深度](CODE/剑指%20Offer%2055%20-%20I.%20二叉树的深度.py)
- [剑指 Offer 55 - II. 平衡二叉树](CODE/剑指%20Offer%2055%20-%20II.%20平衡二叉树.py)
## 堆

[引用自python doc](https://docs.python.org/zh-cn/3.8/library/heapq.html)

堆是一个二叉树，它的每个父节点的值都只会小于或等于所有孩子节点（的值）。 
它使用了数组来实现：从零开始计数，对于所有的 k ，都有 heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2]。
为了便于比较，不存在的元素被认为是无限大。 
堆最有趣的特性在于**最小的元素总是在根结点**：heap[0]。

    定义了以下函数：

    heapq.heappush(heap, item) 时间复杂度： O(log n)
    将 item 的值加入 heap 中，保持堆的不变性。

    heapq.heappop(heap) 时间复杂度：O(log n)
    弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。

    heapq.heappushpop(heap, item)
    将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用 heappush() 再调用 heappop() 运行起来更有效率。

    heapq.heapify(x) 时间复杂度： O(n)
    将list x 转换成堆，原地，线性时间内。

    heapq.heapreplace(heap, item)
    弹出并返回 heap 中最小的一项，同时推入新的 item。 堆的大小不变。 如果堆为空则引发 IndexError。

    这个单步骤操作比 heappop() 加 heappush() 更高效，并且在使用固定大小的堆时更为适宜。 pop/push 组合总是会从堆中返回一个元素并将其替换为 item。

    返回的值可能会比添加的 item 更大。 如果不希望如此，可考虑改用 heappushpop()。 它的 push/pop 组合会返回两个值中较小的一个，将较大的值留在堆中。

复杂度 [最大堆（创建、删除、插入和堆排序）](https://www.jianshu.com/p/21bef3fc3030)
1. 初始化建堆过程时间：O(n)
2. 插入堆元素：O(log n)
3. 删除根节点(只能删除根节点，其他节点删除后只能重建):O(log n)
4. 堆排序：O(nlog n)

Python 默认实现是最小堆，可以用负值的方式实现最大堆:
```python
heap_small = []
heap_big = []

heappush(heap_small, 1)
heappush(heap_big, -1)
heappush(heap_small, 2)
heappush(heap_big, -2)

print(heap_small[0], -heap_big[0]) # output: 1, 2
print(heappop(heap_small), -heappop(heap_big)) # output: 1, 2
```
### 题目
- [剑指 Offer 41. 数据流中的中位数](CODE/剑指%20Offer%2041.%20数据流中的中位数.py)
# 算法总结

## 双指针

### 题目
- [剑指 Offer 58 - I. 翻转单词顺序](CODE/剑指%20Offer%2058%20-%20I.%20翻转单词顺序.py)
- [剑指 Offer 57. 和为s的两个数字](CODE/剑指%20Offer%2057.%20和为s的两个数字.py)

## 动态规划-背包问题
### 思路
- [[总结]动态规划](https://github.com/moshlwx/leetcode/blob/master/CODE/%5B%E6%80%BB%E7%BB%93%5D%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92.py)
- 背包问题九讲
  - 来自 <https://github.com/tianyicui/pack> or <https://www.kancloud.cn/kancloud/pack> 
#### 基本流程
1. 识别定义dp[j]：到第j步
#### 适用场景
1. 背包问题


示例代码
```python
def problem(nums: list):
    dp = [False] * (len(nums)+1)
    dp[0] = True

    for i in range(1, len(nums)+1):
        for j in range(i, -1, -1):
            for k in range(j):
                dp[j] = max(dp[j], dp[j-k]+nums[j-k-1])
    return dp
```
### 题目
- [剑指 Offer 46. 把数字翻译成字符串](CODE/剑指%20Offer%2046.%20把数字翻译成字符串.py)
- [55-跳跃游戏](CODE/55-跳跃游戏.py)
- [剑指 Offer 42. 连续子数组的最大和](CODE/剑指%20Offer%2042.%20连续子数组的最大和.py)
  - 限制连续子数组时需要注意定义dp[i]为截止（包含）当前元素的最大子序列和，然后更新结果变量
- [剑指 Offer 19. 正则表达式匹配](CODE/剑指%20Offer%2019.%20正则表达式匹配.py)
  - 二维动态规划，分状态讨论状态转移公式
- [139. 单词拆分](CODE/139-单词拆分.py)
- [剑指 Offer 60. n个骰子的点数](CODE/剑指%20Offer%2060.%20n个骰子的点数.py)
  - 需要理清楚`DP[i][j]`的概念，前i个骰子和为j的概率，转换为动态规划问题
- [剑指 Offer 47. 礼物的最大价值](CODE/剑指%20Offer%2047.%20礼物的最大价值.py)
- [剑指 Offer 63. 股票的最大利润](CODE/剑指%20Offer%2063.%20股票的最大利润.py)
  - 通过差分计算出每日利润，计算连续最大和即为最佳买卖时机，转换为[连续数组的最大和问题](CODE/剑指%20Offer%2042.%20连续子数组的最大和.py)

## 分治思想

## DFS

### 题目
- [剑指 Offer 28. 对称的二叉树](CODE/剑指%20Offer%2028.%20对称的二叉树.py)
- [139. 单词拆分](CODE/139-单词拆分.py)


## BFS
二叉树的层次遍历
### 基本流程
1. 队列存储每一层选择（根节点）

### 适用场景
1. 二叉树层次遍历
2. 寻找图中最短路径
   
```python
from queue import Queue

q = Queue()
q.put(start)
visited = set()
depth = 0

while not q.empty():
    q_size = q.qsize()

    for _ in range(q_size):
        cur = q.get()
        if cur == target:
            return depth

        for n in neighbor(cur):
            if n and n not in visited:
                q.put(n)
                visited.add(q)
    # 到这里时遍历完一层，深度增加
    depth += 1
# 遍历完没有目标，返回-1
return -1
```

### 题目
- [139. 单词拆分](CODE/139-单词拆分.py)
- [剑指 Offer 55 - I. 二叉树的深度](CODE/剑指%20Offer%2055%20-%20I.%20二叉树的深度.py)
## 滑动窗口

### 题目
- [3. 无重复字符的最长子串](CODE/3-无重复字符的最长子串.py)
- [剑指 Offer 63. 股票的最大利润](CODE/剑指%20Offer%2063.%20股票的最大利润.py)
  - 滑动窗口解法，通过额外保存历史低位值，右指针计算当前与历史低位值的差异，是简化版的滑动窗口
## 二分查找
有序序列中查找目标值或边界的方法，复杂度一般`O(logN)`
### 题目
- [剑指 Offer 57. 和为s的两个数字](CODE/剑指%20Offer%2057.%20和为s的两个数字.py)
  - 一种`O(NlogN)`的解法，通过二分查找有序数组中的目标值，但是10^6的数据量会超时
## 位运算
[Python位运算及运算符优先级](https://www.runoob.com/python/python-operators.html)
<table class="reference">
<tbody><tr><th>运算符</th><th>描述</th></tr>
<tr>
<td>**</td>
<td>指数 (最高优先级)</td>
</tr><tr>
<td>~ + -</td>
<td>按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)</td>
</tr><tr>
<td>* / % //</td>
<td>乘，除，取模和取整除</td>
</tr><tr>
<td>+ -</td>
<td>加法减法</td>
</tr><tr>
<td>&gt;&gt; &lt;&lt;</td>
<td>右移，左移运算符</td>
</tr><tr>
<td>&amp;</td>
<td>位 'AND'</td>
</tr><tr>
<td>^ |</td>
<td>位运算符</td>
</tr><tr>
<td>&lt;= &lt; &gt; &gt;=</td>
<td>比较运算符</td>
</tr><tr>
<td>&lt;&gt; == !=</td>
<td>等于运算符</td>
</tr>
<tr>
<td>= %= /= //= -= += *= **=</td>
<td>赋值运算符</td>
</tr>
<tr>
<td>is is not</td>
<td>身份运算符</td>
</tr>
<tr>
<td>in not in</td>
<td>成员运算符</td>
</tr><tr>
<td>not and or</td>
<td>逻辑运算符</td>
</tr>
</tbody></table>

### 题目
- [剑指 Offer 56 - I. 数组中数字出现的次数](CODE/剑指%20Offer%2056%20-%20I.%20数组中数字出现的次数.py)
