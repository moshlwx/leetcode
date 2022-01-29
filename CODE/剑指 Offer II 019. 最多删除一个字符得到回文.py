'''
剑指 Offer II 019. 最多删除一个字符得到回文
给定一个非空字符串 s，请判断如果 最多 从字符串中删除一个字符能否得到一个回文字符串。

 

示例 1:

输入: s = "aba"
输出: true
示例 2:

输入: s = "abca"
输出: true
解释: 可以删除 "c" 字符 或者 "b" 字符
示例 3:

输入: s = "abc"
输出: false
 

提示:

1 <= s.length <= 10^5
s 由小写英文字母组成
 

注意：本题与主站 680 题相同： https://leetcode-cn.com/problems/valid-palindrome-ii/
'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        基本思路同判断回文。遇到需要跳过的字符，需要分跳过左右的情况讨论
        实际题目不需要考虑符合及大小写问题，暂时保留
        '''
        def subvalidPalindrome(sub_s):
            # 双指针，头尾开始检查
            left = 0
            right = len(sub_s)-1

            while left <= right:
                if not sub_s[left].isalnum():
                    left += 1
                elif not sub_s[right].isalnum() and left < right:
                    right -= 1
                else:
                    if sub_s[left].lower() != sub_s[right].lower():
                        return False
                    left += 1
                    right -= 1

            return True

        if len(s) == 0:
            return True

        # 双指针，头尾开始检查

        left = 0
        right = len(s)-1
        while left <= right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum() and left < right:
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    # 左跳过 右跳过
                    return subvalidPalindrome(s[left: right]) \
                        or subvalidPalindrome(s[left+1: right+1])
                left += 1
                right -= 1
        return True


s = "aba"
# 输出: true
print(Solution().validPalindrome(s))

s = "abca"
# 输出: true
# 解释: 可以删除 "c" 字符 或者 "b" 字符
print(Solution().validPalindrome(s))

s = "abc"
# 输出: false
print(Solution().validPalindrome(s))
