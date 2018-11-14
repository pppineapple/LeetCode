#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:31:48 2018

@author: pineapple
"""

'''
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
            1
          /  \
      null   2
            / \
           3  null

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''

'''
我的：时间复杂度O(n^2) 空间复杂度(1)
思路：递归，专门建立一个类的属性res来维护遍历结果列表
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.inorderTraversal(root.left)
            self.res.append(root.val)
            self.inorderTraversal(root.right)
        return self.res
            
'''
直接递归的代码
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            if root.left:
                res = res + self.inorderTraversal(root.left)
            res.append(root.val)
            if root.right:
                res = res + self.inorderTraversal(root.right)
        return res
    
   
'''
迭代的思路：时间复杂度O(n^2) 空间复杂度O(1)
思路：建立一个类属性self.res表示最终中序遍历结果
    建立一个类属性self.tmp来表示临时栈
    循环的将root的左子节点入栈，直到左子节点为None
    然后出栈node，将节点值加入self.res中
    然后判断node是否有右子节点
    如果有，就将右子节点赋值为root，然后root的左子节点入栈，循环
    循环出口是,root为None和栈为空
'''
class Solution(object):
    def __init__(self):
        self.res = []
        self.tmp = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        while root or self.tmp:
            while root:
                self.tmp.append(root)
                root = root.left
            node = self.tmp.pop()
            self.res.append(node.val)
            if node.right:
                root = node.right
        return self.res