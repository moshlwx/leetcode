'''
763. 划分字母区间
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

示例：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
 

提示：

S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。
'''


class Solution:
    def partitionLabels(self, s: str):
        '''贪心思想，维护每个字母最远位置，遍历字符串，
        若窗口内所有字符对应的最远位置均位于窗口内，则可做划分
        '''
        left = 0
        # right = 0
        res = []

        from collections import Counter

        farest = Counter()
        for i in range(len(s)):
            # 维护每个字母的最远位置
            farest[s[i]] = max(i, farest[s[i]])

        cur_farest = 0

        for i in range(1, len(s)+1):
            cur_farest = max(farest[s[i-1]], cur_farest)

            if i > cur_farest: 
                # print(left, i, s[left: i])
                res.append(i-left)
                left = i
                cur_farest = i

        return res


# 输入：
S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
print(Solution().partitionLabels(S))
