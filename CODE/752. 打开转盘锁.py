'''
752. 打开转盘锁
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

 

示例 1:

输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。
示例 2:

输入: deadends = ["8888"], target = "0009"
输出：1
解释：
把最后一位反向旋转一次即可 "0000" -> "0009"。
示例 3:

输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：
无法旋转到目标数字且不被锁定。
示例 4:

输入: deadends = ["0000"], target = "8888"
输出：-1
 

提示：

死亡列表 deadends 的长度范围为 [1, 500]。
目标数字 target 不会在 deadends 之中。
每个 deadends 和 target 中的字符串的数字会在 10,000 个可能的情况 '0000' 到 '9999' 中产生。
'''


class Solution:
    def openLock(self, deadends, target: str) -> int:
        '''BFS层次遍历，最小深度
        '''
        def neighbor(cur):
            res = []
            for i in [-1, +1]:
                for j in range(len(cur)):
                    ns = int(cur[j]) + i
                    # 处理越界
                    if ns > 9:
                        ns = 0
                    elif ns < 0:
                        ns = 9

                    n = cur[:j] + str(ns) + cur[j+1:]
                    if n not in deadends_set:
                        res.append(n)

            return res
        from queue import Queue

        if target == '0000':
            return 0
        if '0000' in deadends or target in deadends:
            return -1

        q = Queue()
        q.put('0000')
        deadends_set = set(deadends)
        # visited = set()
        min_depth = 0

        while not q.empty():
            q_size = q.qsize()

            for _ in range(q_size):
                cur = q.get()

                if cur == target:
                    # print(cur, deadends_set)
                    return min_depth

                for n in neighbor(cur):
                    q.put(n)
                    deadends_set.add(n)

            min_depth += 1

        return -1


# 输入：
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
# 输出：6
print(Solution().openLock(deadends, target))

# 输入:
deadends = ["8888"]
target = "0009"
# 输出：1
print(Solution().openLock(deadends, target))

# 输入:
deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
target = "8888"
# 输出：-1
# 解释：
# 无法旋转到目标数字且不被锁定。
print(Solution().openLock(deadends, target))

# 输入:
deadends = ["0000"]
target = "8888"
# 输出：-1
print(Solution().openLock(deadends, target))
