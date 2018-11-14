#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 22:29:22 2018

@author: pineapple
"""

'''
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先
且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。
'''

'''
别人的：　时间复杂度O(n) 空间复杂度O(1)
思路：递归
    因为题目说这是　二叉搜索树：即　root.left < root < root.right
    所以ｐ和ｑ的最近公共祖先一定有　p.val <= root.val <= q.val
    上式是假设p.val < q.val，实际函数中会对p.val和q.val取 max 和 min
    
    所以递归思想就是，先对p.val和q.val取 max 和 min
    minn = min(p.val, q.val)
    maxn = max(p.val, q.val)
    如果　minn <= root.val <= maxn　成立，就说明root是最近公共祖先
    否则如果　root.val > maxn，就说明p和q都在root的左子树中，
    只需要递归调用函数　self.lowestCommonAncestor(root.left, p, q)
    否则如果　root.val < minn，就说明p和q都在root的右子树中，
    只需要递归调用函数　self.lowestCommonAncestor(root.right, p, q)
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        minn = min(p.val, q.val)
        maxn = max(p.val, q.val)
        if minn <= root.val <= maxn:
            return root
        elif root.val > maxn:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < minn:
            return self.lowestCommonAncestor(root.right, p, q)