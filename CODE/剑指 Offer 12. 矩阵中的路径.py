'''
剑指 Offer 12. 矩阵中的路径
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。


示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false


提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
board 和 word 仅由大小写英文字母组成


注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/
'''


class Solution:
    def exist(self, board, word: str) -> bool:
        # self.visited = set()

        def neighbor(cur, path):
            '''
            in： (x, y)
            out: [(x, y), (x1, y1)]
            '''
            res = []
            for c in [(cur[0], cur[1]+1), (cur[0], cur[1]-1),
                      (cur[0]+1, cur[1]), (cur[0]-1, cur[1])]:
                if c not in path \
                        and c[0] < len(board) and c[0] >= 0  \
                        and c[1] < len(board[0]) and c[1] >= 0:
                    res.append(c)

            # print('cur:', cur, 'res:', res)
            return res

        def dfs(cur, path):
            '''搜索路径
            '''
            # 若不同则返回
            # print(path)
            if ''.join([board[c[0]][c[1]] for c in path]) != word[:len(path)]:
                return False

            # 若前置任务为真，且长度相同则返回真
            if len(path) == len(word):
                return True

            for c in neighbor(cur, path):
                path.append((c[0], c[1]))

                # 若有符合条件，提前退出
                if dfs(c, path):
                    return True

                path.pop()

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs((i, j), [(i, j)]):
                    return True
        return False


# 输入：
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
# 输出：true
print(Solution().exist(board, word))

# 输入：
board = [["a", "b"], ["c", "d"]]
word = "abcd"
# 输出：false
print(Solution().exist(board, word))

# # 输入：
board = [["a", "a"]]
word = "aaa"
# 输出：false
print(Solution().exist(board, word))

# # 输入：
board = [["a", "b"]]
word = "ba"
# 输出：true
print(Solution().exist(board, word))

# # 输入：
board = [["a", "b"], ["c", "d"]]
word = "bdca"
# 输出：true
print(Solution().exist(board, word))
