r'''
剑指 Offer 28. 对称的二叉树
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
 

限制：

0 <= 节点个数 <= 1000

注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        树的遍历，类似DFS问题，
        递归解决时，先确认退出条件，然后递归调用函数
        '''

        def travel_tree(left_root, right_root):
            '''返回两棵子树是否对称
            '''
            # 结束状态1：叶子节点，则返回真
            if not left_root and not right_root:
                return True

            # 结束状态2：非同时到叶子节点 或值不相等，则返回假
            if not left_root or not right_root or left_root.val != right_root.val:
                return False

            return travel_tree(left_root.left, right_root.right) and travel_tree(left_root.right, right_root.left)

        return travel_tree(root.left, root.right) if root else True


# [1,2,2,3,4,4,3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(Solution().isSymmetric(root))
