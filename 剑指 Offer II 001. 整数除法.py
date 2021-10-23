'''
剑指 Offer II 001. 整数除法
给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%' 。

 

注意：

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231, 231−1]。本题中，如果除法结果溢出，则返回 231 − 1
 

示例 1：

输入：a = 15, b = 2
输出：7
解释：15/2 = truncate(7.5) = 7
示例 2：

输入：a = 7, b = -3
输出：-2
解释：7/-3 = truncate(-2.33333..) = -2
示例 3：

输入：a = 0, b = 1
输出：0
示例 4：

输入：a = 1, b = 1
输出：1
 

提示:

-231 <= a, b <= 231 - 1
b != 0
'''


class Solution:
    def divide_recur(self, a: int, b: int) -> int:
        '''循环减法实现除法，符号逻辑为相同则1为异则-1
        '''
        if b == 0:
            return 2**31-1

        sign = -1 if (a > 0) ^ (b > 0) else 1
        # print(sign)
        res = 0
        cur = abs(a)
        b_abs = abs(b)
        while cur-b_abs >= 0:
            res += 1
            cur -= b_abs

        return sign * res

    def divide(self, a: int, b: int) -> int:
        '''位运算，判断a中含几个b，b从大到小倒序
        '''
        if b == 0:
            return 2**31-1

        sign = -1 if (a > 0) ^ (b > 0) else 1
        a = abs(a)
        b = abs(b)
        res = 0

        # print(sign)
        for n in range(31, -1, -1):
            cur = b << n
            if a >= cur:
                res += 1 << n
                a -= cur

        return sign * res if sign * res < 2**31-1 else 2**31-1  # 溢出时返回最大值


s = Solution()
a = 2147483648
b = 1

print(s.divide(a, b))
