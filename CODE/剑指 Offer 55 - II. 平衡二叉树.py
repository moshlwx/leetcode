r'''
剑指 Offer 55 - II. 平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

 

限制：

0 <= 树的结点个数 <= 10000
注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''递归遍历树，计算深度
        左右孩子若有一个叶子，另一个的深度<1
        分别计算左右子树最大深度，差值超过1则返回假
        '''
        def recur(root):
            '''返回子树的最大深度，若为非平衡二叉树则-1
            '''
            if not root:
                return 0
            
            left = recur(root.left)
            right = recur(root.right)

            if left == -1 or right == -1:
                return -1
            
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1
        