'''
剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 

限制：

1 <= s 的长度 <= 8
'''


class Solution:
    def permutation(self, s: str):
        self.res = set()

        def dfs(choose, path):
            if len(path) == len(s) or not choose:
                self.res.add(''.join(path))

            for i, c in enumerate(choose):
                path.append(c)
                dfs(choose[:i]+choose[i+1:], path)
                path.pop()

        dfs(s, [])

        return [i for i in self.res]


# 输入：
s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
print(Solution().permutation(s))
