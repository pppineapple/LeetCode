# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:11:17 2018

@author: xiaohong
"""

'''
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，
那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
输出: 
合并后的树:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
注意: 合并必须从两个树的根节点开始。
'''

'''
我的 0.97
思路 递归
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        if t1 and t2:
            t = TreeNode(t1.val + t2.val)
        elif t1:
            t = TreeNode(t1.val)
        elif t2:
            t = TreeNode(t2.val)
            
        if t1.left and t2.left:
            t.left = self.mergeTrees(t1.left, t2.left)
        elif t1.left:
            t.left = t1.left
        elif t2.left:
            t.left = t2.left
            
        if t1.right and t2.right:
            t.right = self.mergeTrees(t1.right, t2.right)
        elif t1.right:
            t.right = t1.right
        elif t2.right:
            t.right = t2.right
            
        return t
    
    
'''
别人的优雅代码
'''

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if t1 is None and t2 is None:
            return None
        elif t1 is None:
            return t2
        elif t2 is None:
            return t1
        else:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
        
        
        