'''
剑指 Offer 31. 栈的压入、弹出序列
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

 

示例 1：

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
示例 2：

输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。
 

提示：

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed 是 popped 的排列。
注意：本题与主站 946 题相同：https://leetcode-cn.com/problems/validate-stack-sequences/
'''


class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        '''栈的操作很类似滑动窗口，
        1. for in range(n)
        2. 入栈
        3. 判断需要出栈的元素，while 栈顶与出栈元素相同，则执行出栈
        '''
        stack = []
        i = 0

        for n in pushed:
            stack.append(n)

            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not stack

        '''需要修改传入列表
        for _ in range(n):
            stack.append(pushed[0])
            # remove pushed[0]
            pushed.remove(pushed[0])

            while stack and stack[-1] == popped[0]:
                # stack.pop()
                stack.pop()
                # remove popped[0]
                popped.remove(popped[0])

        return False if popped else True

        '''


# 输入：
pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
# 输出：true

print(Solution().validateStackSequences(pushed, popped))
