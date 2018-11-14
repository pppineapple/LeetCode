#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:32:14 2018

@author: pineapple
"""

'''
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
'''


'''
我的 28ms
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSameTree(p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        p_list = []
        q_list = []
        def preorder(tree_list, tree):
            if tree :
                tree_list.append(tree.val)
                if tree.left == None:
                    tree_list.append('lNone')
                if tree.right == None:
                    tree_list.append('rNone')
                preorder(tree_list, tree.left)
                preorder(tree_list, tree.right)
            
        
        preorder(p_list, p)
        preorder(q_list, q)
        
        if p_list == q_list:
            return True
        else:
            return False
'''
best 24ms
'''        

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
         
        if p==None and q==None:
            return True
        elif p==None and q!=None:
            return False
        elif p!=None and q==None:
            return False
        if p.val!=q.val:
            return False
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)
        return l and r