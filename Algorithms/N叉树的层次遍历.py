# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 21:05:16 2018

@author: xiaohong
"""

'''
给定一个N叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

 

例如，给定一个 3叉树 :
        1
     / |  \
   3   2   4
  / \
 5   6

返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]
'''

'''
我的 时间复杂度O(n^2) 空间复杂度O(n) 1
思路： 利用广度优先搜索BFS的思路利用队列进行层次遍历
        与BFS有差别的是，每次对变量遍历时需要将队列中的节点全部取出
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        output = [[root.val]]
        while queue != []:
            temp = []
            while queue!=[]:
                temp.append(queue.pop(0))
            output_list = []
            for node in temp:
                for i in node.children:
                    output_list.append(i.val)
                    queue.append(i)
            if output_list != []:
                output.append(output_list)
                
        return output
    
'''
简化了一下代码 行树降低了两行
'''
    
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        output = [[root.val]]
        while queue != []:
            count = len(queue)
            output_list = []
            for i in range(count):
                node = queue.pop(0)
                for i in node.children:
                    output_list.append(i.val)
                    queue.append(i)
            if output_list != []:
                output.append(output_list)
        return output