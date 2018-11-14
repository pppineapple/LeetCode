#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 10:54:56 2018

@author: pineapple
"""

'''
序列化是将一个数据结构或者对象转换为连续的比特位的操作，
进而可以将转换后的数据存储在一个文件或者内存中，
同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。
这里不限定你的序列 / 反序列化算法执行逻辑，
你只需要保证一个二叉树可以被序列化为一个字符串
并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，
详情请参阅 LeetCode 序列化二叉树的格式。
你并非必须采取这种方式，
你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，
你的序列化和反序列化算法应该是无状态的。
'''

'''
the time complexity is O(N)
the space complexity is O(N)
别人的：因为没有限定序列化的形式，所以采用DFS来做
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        '''
        'DFS迭代版本，采用栈stack数据结构'
        if not root:
            return 'None'
        stack = [root]
        ans = []
        while stack != []:
            node = stack.pop()
            if node:
                if node.right:
                    stack.append(node.right)
                else:
                    stack.append(None)
                if node.left:
                    stack.append(node.left)
                else:
                    stack.append(None)
                ans.append(str(node.val))
            else:
                ans.append('None')
        return ','.join(ans)
        '''
        'DFS递归版本'
        def dfs(root):
            if not root:
                ans.append('None')
            else:
                ans.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
        ans = []
        dfs(root)
        return ','.join(ans)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        '''
        递归形式
        '''
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')

        if data_list == '':
            return None
        root = rdeserialize(data_list)
        return root
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))