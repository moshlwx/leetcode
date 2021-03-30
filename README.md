# 算法总结

## 动态规划
### 思路
- [[总结]动态规划](https://github.com/moshlwx/leetcode/blob/master/CODE/%5B%E6%80%BB%E7%BB%93%5D%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92.py)
- 背包问题九讲
  - 来自 <https://github.com/tianyicui/pack> or <https://www.kancloud.cn/kancloud/pack> 

#### 动态规划-背包问题
##### 基本流程
1. 识别定义dp[j]：到第j步
##### 适用场景
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
#### 题目
- [剑指 Offer 46. 把数字翻译成字符串](https://github.com/moshlwx/leetcode/blob/master/CODE/%E5%89%91%E6%8C%87%20Offer%2046.%20%E6%8A%8A%E6%95%B0%E5%AD%97%E7%BF%BB%E8%AF%91%E6%88%90%E5%AD%97%E7%AC%A6%E4%B8%B2.py)
- [55-跳跃游戏](https://github.com/moshlwx/leetcode/blob/master/CODE/55-%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8F.py)
- [剑指 Offer 42. 连续子数组的最大和](https://github.com/moshlwx/leetcode/blob/master/CODE/%E5%89%91%E6%8C%87%20Offer%2042.%20%E8%BF%9E%E7%BB%AD%E5%AD%90%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%A4%A7%E5%92%8C.py)
  - 限制连续子数组时需要注意定义dp[i]为截止（包含）当前元素的最大子序列和，然后更新结果变量
- [剑指 Offer 19. 正则表达式匹配](code/剑指%20Offer%2019.%20正则表达式匹配.py)
  - 二维动态规划，分状态讨论状态转移公式
  - 
## 分治思想
## 二叉树
## DFS

#### 题目
- [剑指 Offer 28. 对称的二叉树](CODE/剑指%20Offer%2028.%20对称的二叉树.py)



## BFS
## 滑动窗口
## 二分查找

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