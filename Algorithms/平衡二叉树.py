# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 19:49:12 2018

@author: xiaohong
"""

'''
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

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
'''

'''
我的: 时间复杂度O(n^2) 空间复杂度O(1)
思路： 先建立一个函数递归的求树的深度
        然后递归的去判断root节点下的两颗子树的深度差是不是大于1
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(root):
            if root is None:
                return 0
            return 1+max(depth(root.right), depth(root.left))
        
        if root is None:
            return True
        if root.left or root.right:
            if abs(depth(root.right)-depth(root.left)) > 1:
                return False
            else:
                if not self.isBalanced(root.left):
                    return False
                if not self.isBalanced(root.right):
                    return False
        return True