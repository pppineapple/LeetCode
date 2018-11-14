#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 22:43:04 2018

@author: pineapple
"""

'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''


'''
我的: 时间复杂度O(n) 空间复杂度O(n)
思路：利用队列，结合BFS
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [[root]]
        res = [[root.val]]
        while queue != []:
            nodelist = queue.pop(0)
            subnode = []
            subres = []
            for node in nodelist:
                if node.left:
                    subnode.append(node.left)
                    subres.append(node.left.val)
                if node.right:
                    subnode.append(node.right)
                    subres.append(node.right.val)
            if subnode != []:
                queue.append(subnode)
            if subres != []:
                res.append(subres)
        return res
    

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
s.levelOrder(root)

