r'''
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        '''递归思想重建二叉树
        '''
        if not preorder:
            return None

        root = TreeNode()
        mid_idx = inorder.index(preorder[0])

        preorder_left = preorder[1: mid_idx+1]
        preorder_right = preorder[mid_idx+1:]

        inorder_left = inorder[: mid_idx]
        inorder_right = inorder[mid_idx+1:]

        root.val = preorder[0]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
