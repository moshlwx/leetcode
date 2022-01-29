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

1 <= s.length <= 105
s 由小写英文字母组成
 

注意：本题与主站 680 题相同： https://leetcode-cn.com/problems/valid-palindrome-ii/
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        buffer = 1

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
                    if buffer < 1:
                        return False
                    buffer -= 1
                left += 1
                right -= 1
        

        def sub(sub_s):
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
                        return False
                    left += 1
                    right -= 1

            return True


s = "aba"
print(Solution().validPalindrome(s))