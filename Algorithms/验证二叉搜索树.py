#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 10:26:27 2018

@author: pineapple
"""

'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:输入:
    2
   / \
  1   3
输出: true
示例 2:输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

---------------------

本文来自 dailu11 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/dailu11/article/details/80612801?utm_source=copy 
'''

'''
别人的：　时间复杂度O(n^2) 空间复杂度O(n)
思路：既然是二叉搜索树，然就中序遍历得到每个节点的值组成一个列表
    然后遍历这个列表看是不是升序即可
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        rootlist = []
        self.mid(root, rootlist)
        for i in range(1,len(rootlist)):
            if rootlist[i] <= rootlist[i-1]:
                return False
        return True
               
    def mid(self, root, rootlist):
        if root:
            self.mid(root.left, rootlist)
            rootlist.append(root.val)            
            self.mid(root.right, rootlist)

'''
另外一种递归思路：
从上往下比较的，将每个节点往左就是最大，往右就是最小值，太机智了。
还有就是在传输过程中原函数不能够传递最大最小值，
又重新定义了一个函数调用，值得学习
'''
class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.ValidBST(root, -2**32, 2**32-1)
               
    def ValidBST(self, root, min, max):
        if not root:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.ValidBST(root.left, min, root.val) and self.ValidBST(root.right, root.val, max)
        