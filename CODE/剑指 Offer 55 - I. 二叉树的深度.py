r'''
剑指 Offer 55 - I. 二叉树的深度
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

 

提示：

节点总数 <= 10000
注意：本题与主站 104 题相同：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''二叉树的层次遍历，计算深度，BFS
        '''
        q = Queue()
        q.put(root)
        max_depth = 0
        if not root:
            return max_depth
            
        while not q.empty():
            q_size = q.qsize()

            for _ in range(q_size):
                cur = q.get()

                for t in [cur.left, cur.right]:
                    if t:
                        q.put(t)
            
            max_depth += 1
                
        return max_depth

    def maxDepth(self, root: TreeNode) -> int:
        '''递归思路，二叉树的最大深度为左右子树最大深度+1，叶子节点深度为1
        '''
        # depth = 0
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1