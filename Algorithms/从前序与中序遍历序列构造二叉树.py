#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:40:38 2018

@author: pineapple
"""

'''
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

'''
别人的：　时间复杂度O(logn) 空间复杂度O(n)
思路：递归，递归出口是preorder为[]
    对于前序遍历结果列表preorder,root总是preorder[0]
    对于中序遍历结果列表inorder，先找到root在inorder的索引位置root_index
    root值的左边就是左子树的所有节点，root值的右边就是右子树的所有节点
    所以递归的inorder的两部分就是inorder[:root_index], inorder[root_index+1:]
    递归的preorder的两部分就是preorder[1:root_index+1], preorder[root_index+1:]
    因为在preorder中节点分为三部分[root, root.left, root.right]
    其中所占长度就是[1, 1:root_index+1, root_index+1:]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == []:
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return root