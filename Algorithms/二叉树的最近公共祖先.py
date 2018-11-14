#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 22:57:02 2018

@author: pineapple
"""

'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先
且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
'''


'''
别人的：　时间复杂度O(n),空间复杂度O(1)
思路：递归思想：如果在root的左子树中找到了p(或q),右子树中找到了q(或p)，就返回root
    然后再去左右子树中找看有没有p和q这两个，这里不关心具体p,q在哪一边
    如果左子树中找到了,那么left就不是None，否则是None
    如果右子树中找到了,那么right就不是None，否则是None
    然后对left和right的值进行判断：
    if left and right: 说明左右子树都有点，所以返回root
    elif right:　说明右子树中找到了p和q,那么右子树就是p和q的公共祖先(但不一定是最深)
    elif left:　说明左子树中找到了p和q,那么左子树就是p和q的公共祖先(但不一定是最深)
    所以还需要递归判断
    
    最后还有判断边界条件：
    如果root是None　返回root
    如果p和q有一个节点和root相等，就返回root
    
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
        if not root or root == p or root == q :
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif right:
            return right
        elif left:
            return left
        
        
'''
第二次没做出来，看了答案
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right