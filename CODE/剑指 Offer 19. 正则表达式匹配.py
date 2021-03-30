'''
剑指 Offer 19. 正则表达式匹配
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。
注意：本题与主站 10 题相同：https://leetcode-cn.com/problems/regular-expression-matching/
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        s p两个序列的遍历，二维动态规划
        '''
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]

        dp[0][0] = True

        for j in range(2, len(p)+1, 2):
            dp[0][j] = dp[0][j-2] and p[j-1] == '*'

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    # 当*任意个数时，任意为真则为匹配
                    # 1. *=0 2.
                    # 2. *前一位=s的位
                    # 3. *前一位是'.'
                    dp[i][j] = dp[i][j-2] \
                        or (dp[i-1][j] and p[j-2] == s[i-1]) \
                        or (dp[i-1][j] and p[j-2] == '.')

                else:
                    # 当其他字符
                    dp[i][j] = (dp[i-1][j-1] and p[j-1] == '.') \
                        or (dp[i-1][j-1] and p[j-1] == s[i-1])

        return dp[-1][-1]


        # 输入:
s = "mississippi"
p = "mis*is*p*."
# 输出: false
s = "aab"
p = "c*a*b"

print(Solution().isMatch(s, p))
