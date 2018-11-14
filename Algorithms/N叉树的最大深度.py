# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:48:20 2018

@author: xiaohong
"""

max([1,2,3])
[1,2,3].max()


'''
我的 0.97
思路：递归
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        '''BFS'''
        if root is None:
            return 0
        if root.children == []:
            return 1
        
        return 1 + max([self.maxDepth(node) for node in root.children])
    
    def maxDepth(self, root)
        '''DFS'''
        if root is None:
            return 0
        queue = [root]
        depth = 0
        while queue != []:
            depth += 1
            for i in range(len(queue)):
                for child in queue[0].children:
                    queue.append(child)
                queue.pop(0)
        return depth