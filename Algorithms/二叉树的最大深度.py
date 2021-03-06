# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 20:31:30 2018

@author: xiaohong
"""

'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    '''DFS'''
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0        
        queue = [root]
        depth = 0
        while queue != []:
            depth += 1
            for i in range(len(queue)):
                if queue[0].left is not None:
                    queue.append(queue[0].left)
                if queue[0].right is not None:
                    queue.append(queue[0].right)
                queue.pop(0)
            
        return depth
    
    '''BFS'''
    '''二分，递归'''
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''树的深度=max(左子树深度，右子树深度) + 1'''
        if root is None:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1    
    
'''
第二次做：

'''
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
'''
第三次做
'''

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))