#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:30:21 2018

@author: pineapple
"""

'''
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
'''

'''
别人的：　时间复杂度O(n^2) 空间复杂度O(1)
思路：　因为是二叉搜索树，所以root.left < root < root.right，
    计算左左子树的节点数:left
if left == k - 1, 说明root就是第k小的数，return root.val
if left >= k，说明第k小的数就在左子树之中，递归调用函数 func(self.left, k)
if left < k - 1，说明第k小的数在右子树中，递归调用函数　func(self.right, k-left-1)
        
'''

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #print self.countnode(root.left)
        leftcount = self.countnode(root.left)
        if leftcount == k-1:
            return root.val
        elif leftcount >= k:
            return self.kthSmallest(root.left, k)
        elif leftcount < k -1:
            return self.kthSmallest(root.right, k-leftcount-1)
        
    def countnode(self, root):
        if not root:
            return 0
        else:
            return 1 + self.countnode(root.left) + self.countnode(root.right)
    
'''
第二次做
'''    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root:          
            left = self.treenodecount(root.left)
            if left > k-1:
                return self.kthSmallest(root.left, k)
            elif left == k-1:
                return root.val
            elif left < k-1:
                return self.kthSmallest(root.right, k-left-1)
      
    def treenodecount(self,root):
        if not root:
            return 0
        return 1 + self.treenodecount(root.left) + self.treenodecount(root.right)
        
        
'''
更快的代码：时间复杂度O(logn) 空间复杂度O(1)
思路：以为二叉搜索树的中序遍历是有序的
    所以可以直接对二叉搜索树进行中序遍历
    建立两个属性self.cur和self.ans表示，当前遍历的记得点的位置数(有序)和最终k的值
    中序遍历时，用self.cur+=1记录位置
    当self.cur==k时，就说明root.val就是要找的第k小的值
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cur = 0
        self.ans = None
        def inordersearch(root):
            if not root:
                return
            inordersearch(root.left)
            self.cur += 1
            if self.cur == k:
                self.ans = root.val
                return 
            inordersearch(root.right)
        inordersearch(root)
        return self.ans
    
tree = TreeNode(3)
tree.left = TreeNode(1)
tree.right = TreeNode(4)
tree.left.right = TreeNode(2)
s = Solution()
s.kthSmallest(tree,1)
