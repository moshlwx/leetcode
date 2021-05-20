[toc]
# 数据结构
## 栈
### 题目
- [剑指 Offer 31. 栈的压入、弹出序列](CODE/剑指%20Offer%2031.%20栈的压入、弹出序列.py)

## 二叉树
二叉树大部分涉及递归思想
### 题目
- [剑指 Offer 28. 对称的二叉树](CODE/剑指%20Offer%2028.%20对称的二叉树.py)
- [236. 二叉树的最近公共祖先](CODE/236.%20二叉树的最近公共祖先.py)
- [105. 从前序与中序遍历序列构造二叉树](CODE/105.%20从前序与中序遍历序列构造二叉树.py)
- [剑指 Offer 55 - I. 二叉树的深度](CODE/剑指%20Offer%2055%20-%20I.%20二叉树的深度.py)
- [剑指 Offer 55 - II. 平衡二叉树](CODE/剑指%20Offer%2055%20-%20II.%20平衡二叉树.py)
## 堆

[引用自python doc](https://docs.python.org/zh-cn/3.8/library/heapq.html)

堆是一个二叉树，它的每个父节点的值都只会小于或等于所有孩子节点（的值）。 
它使用了数组来实现：从零开始计数，对于所有的 k ，都有 `heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2]`。
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

- [[总结]动态规划](https://github.com/moshlwx/leetcode/blob/master/CODE/%5B%E6%80%BB%E7%BB%93%5D%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92.py)
- 背包问题九讲
  - 来自 <https://github.com/tianyicui/pack> or <https://www.kancloud.cn/kancloud/pack> 
- [暴力解法、动态规划（Java）](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/bao-li-mei-ju-dong-tai-gui-hua-chai-fen-si-xiang-b/)
- [股票问题系列通解（转载翻译）](https://leetcode-cn.com/circle/article/qiAgHn/)

### 基本流程
1. 识别定义`dp[j]`：到第j步时目标值的状态
2. 输出状态转移公式`dp[j] = func(dp[j-1], nums[j-1-k])`

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

### 适用场景
1. 背包问题
2. O(N)复杂度的遍历问题

### 题目
- [剑指 Offer 46. 把数字翻译成字符串](CODE/剑指%20Offer%2046.%20把数字翻译成字符串.py)
- [55-跳跃游戏](CODE/55-跳跃游戏.py)
- [剑指 Offer 42. 连续子数组的最大和](CODE/剑指%20Offer%2042.%20连续子数组的最大和.py)
  - 限制连续子数组时需要注意定义dp[i]为截止（包含）当前元素的最大子序列和，然后更新结果变量
- [剑指 Offer 19. 正则表达式匹配](CODE/剑指%20Offer%2019.%20正则表达式匹配.py)
  - 二维动态规划，分状态讨论状态转移公式
- [139. 单词拆分](CODE/139.%20单词拆分.py)
- [剑指 Offer 60. n个骰子的点数](CODE/剑指%20Offer%2060.%20n个骰子的点数.py)
  - 需要理清楚`DP[i][j]`的概念，前i个骰子和为j的概率，转换为动态规划问题
- [剑指 Offer 47. 礼物的最大价值](CODE/剑指%20Offer%2047.%20礼物的最大价值.py)
- [剑指 Offer 63. 股票的最大利润](CODE/剑指%20Offer%2063.%20股票的最大利润.py)
  - 通过差分计算出每日利润，计算连续最大和即为最佳买卖时机，转换为[连续数组的最大和问题](CODE/剑指%20Offer%2042.%20连续子数组的最大和.py)
- [714. 买卖股票的最佳时机含手续费](CODE/714.%20买卖股票的最佳时机含手续费.py)
  - [暴力解法、动态规划（Java）](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/bao-li-mei-ju-dong-tai-gui-hua-chai-fen-si-xiang-b/)
  - [股票问题系列通解（转载翻译）](https://leetcode-cn.com/circle/article/qiAgHn/)
- [剑指 Offer 13. 机器人的运动范围](CODE/剑指%20Offer%2013.%20机器人的运动范围.py)
  - 动态规划解法暂未实现，参考[剑指 Offer 47. 礼物的最大价值](CODE/剑指%20Offer%2047.%20礼物的最大价值.py)，二者场景很像
- [322. 零钱兑换](CODE/322.%20零钱兑换)
- [494. 目标和](CODE/494.%20目标和.py) 
  - DFS暴力遍历会超复杂度，此类场景考虑记忆化or直接用DP
## 贪心算法

### 基本步骤
1. 暴力解法理清思路
2. 通过贪心思想优化
   1. 只关注最值/极值，裁剪次高值的遍历
   2. 局部最优替代全局最优

#### 不重叠区间基本步骤
1. 按照区间结束坐标排序区间
2. 循环所有区间，若区间开始点大于（等于视题目要求算是否重叠）上个结束区间则认为不重叠，加入不重叠区间的集合

```python
# 按照结束区间倒序
intervals_sorted = sorted(intervals, key=(lambda x: x[1]))
intervals_min = []
last_end = float('-inf')

# 选择最早结束的区间，删除所有相交的区间
for i in intervals_sorted:
    # 相交属于重叠则>，不算重叠则>=
    if i[0] >= last_end:
        intervals_min.append(i)
        last_end = i[1]
```
### 常见应用
1. 求不重叠子区间
2. DFS/BFS/动态规划算法超复杂度的场景，相当利用局部最优特性减少遍历范围

### 题目
- [435. 无重叠区间](CODE/435.%20无重叠区间.py)
- [452. 用最少数量的箭引爆气球](CODE/452.%20用最少数量的箭引爆气球.py)
  - 气球边界接触也算作重叠，所以判断不重叠时`当前起点>上个区间的终点`，与435区别仅在`>=`
- [55. 跳跃游戏](CODE/55.%20跳跃游戏.py)
- [45. 跳跃游戏 II](CODE/45.%20跳跃游戏%20II.py)
  - https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0045.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8FII.md
- [621. 任务调度器](CODE/621.%20任务调度器.py)
  - 做调度规划，贪心思想体现在：只需要安排最多任务，次多任务不会影响最终结果。
- [406. 根据身高重建队列](CODE/406.%20根据身高重建队列.py)
  - 贪心优化的思路类似任务调度器，次高身高的人不会影响高人的相对顺序，所以只需要按照身高降序插入对应位置即可
- [134. 加油站](CODE/134.%20加油站.py)
  - 基于暴力解法优化，下次遍历从当前能到达的最远加油站开始，复杂度减少到O(N)
- [763. 划分字母区间](CODE/763.%20划分字母区间.py)

## 分治思想

## DFS
### 基本流程
1. 递归尝试所有选择
2. 判断满足终止条件时更新路径，返回

```python
def dfs(path: list, choose: list):
    # 判断返回
    if len(path) == len(target) or not choose:  # 或其他满足条件
        # 注意这里用path的深拷贝，避免浅拷贝产生引用
        res.append(path.copy())
        return
    # 递归尝试所有选择
    for c in choose:
        path.append(c)
        dfs(path, choose-c)
        path.pop()

target = [1, 2, 3, 4]
res = []
choose = [1, 23, 4]
dfs([], choose)
print(res)
```

### 适用场景
1. 全排列
2. 所有可能性的一种遍历方法，复杂度同BFS
### 题目
- [剑指 Offer 28. 对称的二叉树](CODE/剑指%20Offer%2028.%20对称的二叉树.py)
- [139. 单词拆分](CODE/139-单词拆分.py)
- [剑指 Offer 13. 机器人的运动范围](CODE/剑指%20Offer%2013.%20机器人的运动范围.py)
- [406. 根据身高重建队列](CODE/406.%20根据身高重建队列.py)
  - 数据量较大，全量遍历会超时。
- 全排列
  - [46. 全排列](CODE/46.%20全排列.py)
  - [剑指 Offer 38. 字符串的排列](CODE/剑指%20Offer%2038.%20字符串的排列.py)
- [494. 目标和](CODE/494.%20目标和.py)
- [111. 二叉树的最小深度](CODE/111.%20二叉树的最小深度.py)
  - 深度优先遍历整棵树，  当前深度超过最小深度时裁剪
- 路径和问题
  - [剑指 Offer 34. 二叉树中和为某一值的路径](CODE/剑指%20Offer%2034.%20二叉树中和为某一值的路径.py)
  - [494. 目标和](CODE/494.%20目标和.py) DFS暴力遍历会超复杂度，考虑记忆化or直接用DP

## BFS
二叉树的层次遍历
### 基本流程
1. 队列存储每一层选择（根节点）

```python
from queue import Queue
q = Queue()
q.put(start)
visited = set()
depth = 0
while not q.empty():
    q_size = q.qsize()
    row = []
    for _ in range(q_size):
        cur = q.get()
        # 每层的记录在先序做，后序会需要较多的空值处理
        row.append(cur.val)

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
- [剑指 Offer 13. 机器人的运动范围](CODE/剑指%20Offer%2013.%20机器人的运动范围.py)
- [102. 二叉树的层序遍历](CODE/102.%20二叉树的层序遍历.py)
- [107. 二叉树的层序遍历 II](CODE/107.%20二叉树的层序遍历%20II.py)
- [剑指 Offer 32 - I. 从上到下打印二叉树](CODE/剑指%20Offer%2032%20-%20I.%20从上到下打印二叉树.py)
- [剑指 Offer 32 - II. 从上到下打印二叉树](CODE/剑指%20Offer%2032%20-%20II.%20从上到下打印二叉树%20II.py)
- [剑指 Offer 32 - III. 从上到下打印二叉树](CODE/剑指%20Offer%2032%20-%20III.%20从上到下打印二叉树%20III.py)
- [111. 二叉树的最小深度](CODE/111.%20二叉树的最小深度.py)
  - 层次遍历，遇到叶子节点即结束返回当前深度
- [127. 单词接龙](CODE/127.%20单词接龙.py)
  - 多叉树的层次遍历，遇到目标值即结束返回当前深度
- [752. 打开转盘锁](CODE/752.%20打开转盘锁.py)
  - 多叉树的层次遍历，遇到目标值即结束返回当前深度
  
## 滑动窗口
### 基本流程
1. 移动右边界，更新窗口
2. while左边界需要收缩，收缩左边界，更新窗口
3. 窗口满足跳出条件，更新返回值

```python
def sliding_window(s: str, t: str):
    '''基础问题，给定来源字符串s，找到符合t目标的窗口，or符合t目标的最值
    '''
    # 利用python collections.Counter类型统计频次，更方便操作，正常可用数组或字典代替
    from collections import Counter
    left = 0
    right = 0
    window = Counter()
    # s_counter = Counter(s)
    # t_counter = Counter(t)
    valid_flag = False
    res = 0
    while right < len(s):
        # 暂存入窗口值，移动右边界
        c = s[right]
        right += 1
        # 更新窗口内数据
        window[c] += 1
        valid_flag = True if True else False
        while not valid_flag: # 当不满足限制时，更新左边界
            d = s[left]
            left += 1
            # 更新窗口内数据
            window[d] -= 1
            valid_flag = True if True else False
        # 窗口更新完毕，此时窗口内状态满足while条件的跳出值，常在这里更新返回值
        res = max(res, right - left)
    return res
```
### 适用场景
基础问题，给定来源字符串s，找到符合t目标的窗口，or符合t目标的最值

### 题目
- [3. 无重复字符的最长子串](CODE/3-无重复字符的最长子串.py) and [剑指 Offer 48. 最长不含重复字符的子字符串](CODE/剑指%20Offer%2048.%20最长不含重复字符的子字符串.py)
- [剑指 Offer 63. 股票的最大利润](CODE/剑指%20Offer%2063.%20股票的最大利润.py)
  - 滑动窗口解法，通过额外保存历史低位值，右指针计算当前与历史低位值的差异，是简化版的滑动窗口

## 二分查找
### 适用场景
有序序列中查找目标值或边界的方法，复杂度一般`O(logN)`
### 基本流程

```python
def binary_search(nums: list, target: int):
    left = 0
    right = len(nums) - 1
    while left <= right:
        # use // to get int result, revode error when nums[mid]
        mid = left + (right-left)//2
        if nums[mid] < target:  # target in right half
            left = mid + 1
        elif nums[mid] > target:  # in left half
            right = mid - 1
        else:  # nums[mid] == target
            return mid
    # no return after loop, return -1
    return -1

def binary_left_bound(nums: list, target: int):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            right = mid - 1  # 区别点：nums[mid] == target时不返回，锁定左侧边界，更新右边界

    # 检查越界、目标值不存在的情况，返回默认值
    if left >= len(nums) or nums[left] != target:
        return -1
    return left

def binary_right_bound(nums: list, target: int):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right-left)//2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid - 1  # 区别点：nums[mid] == target时不返回，锁定右侧边界，更新左边界

    # 检查越界、目标值不存在的情况，返回默认值
    if right < 0 or nums[right] != target:
        return -1
    return right
```
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
