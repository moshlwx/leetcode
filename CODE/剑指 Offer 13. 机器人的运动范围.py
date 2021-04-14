'''
剑指 Offer 13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
'''


class Solution:
    def check_range(self, x, y):
        '''检查x,y是否合法返回真假
        1. 上下界在m,n内，不为负数
        2. 数位和<k
        '''
        # ？？？作为类函数时，不能直接使用调用函数的变量，本地IDE不报错，力扣会报错
        if not (x < m and x >= 0 and y < n and y >= 0):
            return False

        xs = sum([int(i) for i in str(x)])
        ys = sum([int(i) for i in str(y)])

        if xs+ys > k:
            return False
        return True

    def movingCount_dfs(self, m: int, n: int, k: int):
        '''dfs深度优先遍历
        '''
        self.res = set()
        self.path = []

        def dfs(x, y):
            self.path.append((x, y))
            if (x, y) in self.res or not self.check_range(x, y):
                return

            self.res.add((x, y))

            for i in [-1, 1]:
                dfs(x, y+i)
                dfs(x+i, y)

        dfs(0, 0)
        # print(self.path)
        # print(self.res)
        return len(self.res)

    def movingCount_bfs(self, m: int, n: int, k: int):
        '''bfs层次遍历
        '''
        from queue import Queue
        q = Queue()
        visited = set()
        q.put((0, 0))
        visited.add((0, 0))

        while not q.empty():
            cur = q.get()

            for c in [(cur[0], cur[1]+1), (cur[0], cur[1]-1),\
                 (cur[0]+1, cur[1]), (cur[0]-1, cur[1])]:
                if c not in visited and check_range(c[0], c[1]):
                    q.put(c)
                    visited.add(c)
        # print(visited)
        return len(visited)

    def movingCount(self, m: int, n: int, k: int):
        '''动态规划(未运行通过)
        dp[x][y]，运动范围为x,y时，可达个数
        dp[i][j] = max(dp[i][j-1]+check_range(i, j), dp[i-1][j]+check_range(i, j))
        '''
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # dp[0][0] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i][j-1]
                               + sum([self.check_range(ii, j)
                                      for ii in range(1, i+1)]),
                               dp[i-1][j]
                               + sum([self.check_range(i, ji) for ji in range(1, j+1)]))

        return dp[-1][-1]


# 输入：
m = 10
n = 5
k = 10
# 输出：3
print(Solution().movingCount_dfs(m, n, k))
