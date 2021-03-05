'''动态规划-背包问题
# 基本流程
1. 识别定义dp[j]：到第j步

# 适用场景
1. 背包问题
2. 
'''

def problem(nums: list):
    dp = [False] * (len(nums)+1)
    dp[0] = True

    for i in range(1, len(nums)+1):
        for j in range(i, -1, -1):
            for k in range(j):
                dp[j] = max(dp[j], dp[j-k]+nums[j-k-1])

    return dp