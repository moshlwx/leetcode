'''
剑指 Offer 58 - I. 翻转单词顺序
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

 

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
注意：本题与主站 151 题相同：https://leetcode-cn.com/problems/reverse-words-in-a-string/

注意：此题对比原题有改动
'''


class Solution:
    def reverseWords(self, s):
        '''双指针，反向遍历截取单词，
        '''
        res = []
        s = s.strip()
        left = len(s) - 1
        right = len(s) - 1

        while left >= 0:
            # 当非空字符时左边界移动
            while left >= 0 and s[left] != ' ':
                left -= 1
            res.append(s[left+1: right+1])
            # 当空格时继续左移边界
            while s[left] == ' ':
                left -= 1
            right = left
        return ' '.join(res)

    def reverseWords_split_reverse(self, s: str) -> str:
        s_list = s.split()
        # s_list.re('')
        s_list.reverse()
        print(s_list)
        return ' '.join(s_list)


s = "a good example"
print(Solution().reverseWords(s))
