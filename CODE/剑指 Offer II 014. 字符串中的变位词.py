'''
剑指 Offer II 014. 字符串中的变位词
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的某个变位词。

换句话说，第一个字符串的排列之一是第二个字符串的 子串 。

 

示例 1：

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
示例 2：

输入: s1= "ab" s2 = "eidboaoo"
输出: False
 

提示：

1 <= s1.length, s2.length <= 104
s1 和 s2 仅包含小写字母
 

注意：本题与主站 567 题相同： https://leetcode-cn.com/problems/permutation-in-string/
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''滑动窗口
        窗口内Count与目标Count完全一致
        '''
        res = False

        from collections import Counter

        target_count = Counter(s1)
        window_count = Counter()
        target_len = len(s1)

        left = 0
        right = 0

        while right < len(s2):
            c = s2[right]
            right += 1
            window_count[c] += 1

            while window_count[c] > target_count[c] and left < right:
                d = s2[left]
                left += 1
                window_count[d] -= 1

            # 全量比对窗口成本有点高，应该可以只比对增量
            # print('window[%d: %d] = %s' % (left, right, s2[left: right]))
            if right-left == target_len:
                return True

        return res


# 输入:
s1 = "hello"

s2 = "ooolehoooleh"
# 输出: True
print(Solution().checkInclusion(s1, s2))
