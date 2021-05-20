r'''
剑指 Offer 34. 二叉树中和为某一值的路径
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

示例:
给定如下二叉树，以及目标和 target = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
 

提示：

节点总数 <= 10000
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int):
        '''
        DFS遍历树，记录路径和
        '''
        if not root:
            return []

        self.res = []

        def dfs(choose, path):
            if not choose:
                if sum(path) == target:
                    self.res.append(path.copy())
                return
            
            for n in [choose.left, choose.right]:
                path.append(n.val)
                dfs(n, path)
                path.pop()

        dfs(root, [root])
        return self.res
