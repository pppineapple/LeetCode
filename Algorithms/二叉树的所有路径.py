# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 19:41:42 2018

@author: xiaohong
"""
'''
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
'''

'''
我的 时间复杂度O(n), 空间复杂度O(n) 0.98
思路， DFS 使用栈
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        
        output = []
        path = [str(root.val)]
        stack = [root]
        while stack != []:
            node = stack.pop()
            node_path = path.pop()
            if node.left:
                lnode_path = node_path + '->' + str(node.left.val)
                stack.append(node.left)
                path.append(lnode_path)
            if node.right:
                rnode_path = node_path + '->' + str(node.right.val)
                stack.append(node.right)
                path.append(rnode_path)
            if node.left is None and node.right is None:
                output.append(node_path)
                
        return output
 
'''
优雅的代码 1
思路： 递归
'''               
            
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        out = []
        return self.path(root, out, str(root.val))
        
        
        
    def  path(self, root, out, string):
        if root.left is None and root.right is None:
            out.append(string+'->'+str(root.val))
        if root.left:
            self.path(root.left, out, string+'->'+str(root.left.val))
        if root.right:
            self.path(root.right, out, string+'->'+str(root.right.val))   
        return out
                
            