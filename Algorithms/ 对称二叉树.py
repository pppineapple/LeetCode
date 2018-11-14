#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 22:10:44 2018

@author: pineapple
"""

'''
给定一个二叉树，检查它是否是镜像对称的。

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
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
'''


'''
别人的：　时间复杂度O(nlogn) 空间复杂度O(n)
思路：编写一个辅助函数从上到下递归判断左右子树对称位置是否相同
    递归出口是，是比较的两个节点都是none
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.judge(root.left, root.right)
            
    def judge(self, left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return self.judge(left.left, right.right) and self.judge(left.right, right.left)
        else:
            return False