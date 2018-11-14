# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:02:04 2018

@author: xiaohong
"""
'''
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
'''


'''
我的 时间复杂度O(n) 空间复杂度O(1) 1
思路： 通常二叉树，我就会考虑递归的去变换左右节点，冲root一直到叶节点。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
                
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root