'''
剑指 Offer II 013. 二维子矩阵的和
给定一个二维矩阵 matrix，以下类型的多个请求：

计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
实现 NumMatrix 类：

NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
int sumRegion(int row1, int col1, int row2, int col2) 返回左上角 (row1, col1) 、右下角 (row2, col2) 的子矩阵的元素总和。
 

示例 1：



输入: 
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
输出: 
[null, 8, 11, 12]

解释:
NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-105 <= matrix[i][j] <= 105
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
最多调用 104 次 sumRegion 方法
 

注意：本题与主站 304 题相同： https://leetcode-cn.com/problems/range-sum-query-2d-immutable/

通过次数4,705提交次数7,165
'''


class NumMatrix:
    '''
    矩阵大小不大，但是查询次数多，考虑用初始化复杂度换取降低查询复杂度
    初始化时，计算从原点到当前坐标的子矩阵和。
    任意起止坐标的子矩阵和为 sum[(终点)] + sum[(起点)]-sum[(row1, col2)]-sum[(row2, col1)]
    '''

    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_sum = [
            [0 for j in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]

        for i in range(len(matrix)):
            cur_sum = 0
            for j in range(len(matrix[0])):
                cur_sum += matrix[i][j]
                self.matrix_sum[i][j] = cur_sum + self.matrix_sum[i-1][j]

        # print(self.matrix_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        res = self.matrix_sum[row2][col2] - self.matrix_sum[row1-1][col2] - \
            self.matrix_sum[row2][col1-1] + self.matrix_sum[row1-1][col1-1]

        return res

    def sumRegion_baoli(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2 + 1):
                res += self.matrix[i][j]

        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# 输入:
# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# 输出:
# [null, 8, 11, 12]
matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [
    1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
s = NumMatrix(matrix)

print(s.sumRegion(2, 1, 4, 3))
print(s.sumRegion(1, 1, 2, 2))
print(s.sumRegion(1, 2, 2, 4))
