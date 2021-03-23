# 算法总结

## 【算法】动态规划
### 思路
[[总结]动态规划](https://github.com/moshlwx/leetcode/blob/master/CODE/%5B%E6%80%BB%E7%BB%93%5D%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92.py)
#### 动态规划-背包问题
##### 基本流程
1. 识别定义dp[j]：到第j步
##### 适用场景
1. 背包问题
2. 
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