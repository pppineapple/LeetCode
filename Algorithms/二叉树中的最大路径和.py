#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 22:00:35 2018

@author: pineapple
"""

'''
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。
该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42
'''

'''
别人的: 时间复杂度O(n^2) 空间复杂度O(1)
思路：递归思想。
    判断一颗树的最大和路径，
    就是等于root.val + 左子数的最大和路径的一半 + 右子数的最大和路径的一半
    然后建立一个全局变量maxpathsum来更新路径最大和
    新建一个方法maxsum(root)用来计算树的最大和路径，递归思想
    先计算左字数的路径最大和，再计算右子树路径最大和，
    注意这里的路径最大和只是一半的，即 root.val+lsum　和　root.val+rsum
    然后要判断左子树的最大路径和是否小于０，如果小于０，就赋值为０
    然后要判断右子树的最大路径和是否小于０，如果小于０，就赋值为０
    然后，以root为根节点的树的最大路径和就是 sum = root.val + lsum + rsum
    这个时候，更新全局变量　self.maxpathsum = max(self.maxpathsum, sum)
    最后 maxpathsum　要返回最大的路径和　
    max(root.val, max(root.val+lsum, root.val+rsum))
    用来保证递归完整进行
    
    整体的函数 maxPathSum(root)　返回的是全局变量 maxpathsum
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxpathsum = float('-inf')
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxsum(root)
        return self.maxpathsum   
    
    def maxsum(self, root):
        if not root:
            return 0
        sum = root.val
        lsum = 0
        rsum = 0
        if root.left:
            lsum = self.maxsum(root.left)
            if lsum > 0:
                sum += lsum
        if root.right:
            rsum = self.maxsum(root.right)
            if rsum > 0:
                sum += rsum
        self.maxpathsum = max(self.maxpathsum, sum)        
        return max(root.val, max(root.val+lsum, root.val+rsum))
    
'''
第二遍：没做出来，看了答案
'''

class Solution(object):
    def __init__(self):
        self.maxPathSumValue = float('-inf')
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum(root)
        return self.maxPathSumValue
             
    def maxSum(self, root):
        if not root:
            return 0
        sum = root.val
        lsum = 0
        rsum = 0
        if root.left:
            lsum = self.maxSum(root.left)
            if lsum > 0:
                sum += lsum
        if root.right:
            rsum = self.maxSum(root.right)
            if rsum > 0:
                sum += rsum
        self.maxPathSumValue = max(self.maxPathSumValue, sum)
        return max(root.val, max(root.val+lsum, root.val+rsum))
            
    
    
    
    
    