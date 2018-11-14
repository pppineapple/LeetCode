#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 12:18:42 2018

@author: pineapple
"""


'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。
（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
'''

'''
我的：时间复杂度O(n^2) 空间复杂度O(n)
思路：还是按照BFS遍历树，每次遍历都是从左到右
    但是，要设置一个变量i来决定是不是耀反转这层遍历的结果
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [[root]]
        res = [[root.val]]
        i = 1
        while queue != []:
            node = queue.pop(0)
            tmp = []
            tmp_val = []
            for u in node:
                if u.left:
                    tmp.append(u.left)
                    tmp_val.append(u.left.val)
                if u.right:
                    tmp.append(u.right)
                    tmp_val.append(u.right.val)           
            if tmp_val != []:
                queue.append(tmp)
                if i % 2 != 0:
                    res.append(tmp_val[::-1])
                else:
                    res.append(tmp_val)
            i += 1
        return res