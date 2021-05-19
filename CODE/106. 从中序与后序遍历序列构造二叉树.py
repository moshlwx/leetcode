r'''
106. 从中序与后序遍历序列构造二叉树
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        '''二叉树的遍历，递归方法解决
        '''
        if not inorder:
            return None
        root = TreeNode(postorder[-1])

        mid_idx = inorder.index(postorder[-1])

        inorder_left = inorder[: mid_idx]
        inorder_right = inorder[mid_idx+1:]

        postorder_left = postorder[: mid_idx]
        postorder_right = postorder[mid_idx: -1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root
