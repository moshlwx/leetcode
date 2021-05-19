'''
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
 

提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
'''


class Solution:
    def permute(self, nums):
        '''DFS思路
        '''
        self.res = []

        def dfs(choose, path):
            if len(path) == len(nums):
                # print(path)
                self.res.append(path.copy())
                return
            if not choose:
                return

            for i, c in enumerate(choose):
                path.append(c)
                dfs(choose[:i]+choose[i+1:], path)
                path.pop()

        dfs(nums, [])

        return self.res


# 输入：
nums = [1, 2, 3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 示例 2：
print(Solution().permute(nums))

# 输入：
nums = [0, 1]
# 输出：[[0,1],[1,0]]
# 示例 3：
print(Solution().permute(nums))

# 输入：
nums = [1]
# 输出：[[1]]
print(Solution().permute(nums))

# 输入：
nums = []
# 输出：[[]]
print(Solution().permute(nums))