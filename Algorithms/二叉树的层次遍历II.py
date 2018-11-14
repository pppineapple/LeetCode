# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 21:11:38 2018

@author: xiaohong
"""

'''
给定一个二叉树，返回其节点值自底向上的层次遍历。 
（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
别人的 0.97
思路， 广度优先搜索BFS 利用队列，记录出队的节点，组成列表查到结果列表的首位
'''

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        output = []
        queue = [root]
        while queue != []:
            node = []
            for i in range(len(queue)):                
                if queue[0].left is not None:
                    queue.append(queue[0].left)
                if queue[0].right is not None:
                    queue.append(queue[0].right)
                temp = queue.pop(0)  
                node.append(temp.val)
            output.insert(0, node)
        return output