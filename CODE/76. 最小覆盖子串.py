'''
76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
 

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        min_len = float('inf')
        vaild_cnt = 0
        res = ''

        from collections import Counter
        window = Counter()

        while right < len(s):
            c = s[right]
            right += 1

            window[c] += 1

            if c in t and window[c] == 1:
                vaild_cnt += 1

            # 当window覆盖所有t的子串
            while vaild_cnt == len(t):
                d = s[left]
                left += 1

                window[d] -= 1

                if d in t and window[d] == 0:
                    vaild_cnt -= 1

            if right-left < min_len:
                res = s[left: right]
                min_len = right - left

        return res
                
# 输入：
s = "ADOBECODEBANC"
t = "ABC"
# 输出："BANC"
print(Solution().minWindow(s, t))