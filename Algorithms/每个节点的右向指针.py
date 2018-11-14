#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:18:15 2018

@author: pineapple
"""
'''
给定一个二叉树

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。
如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

说明:

你只能使用额外常数空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
你可以假设它是一个完美二叉树（即所有叶子节点都在同一层，每个父节点都有两个子节点）。
示例:

给定完美二叉树，

     1
   /  \
  2    3
 / \  / \
4  5  6  7
调用你的函数后，该完美二叉树变为：

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
'''


'''
我的：　时间复杂度O(n) 空间复杂度O(n)
思路：利用BFS和队列queue遍历完美二叉树，然后在每层树遍历时
    用列表tmp来储存这一层的节点，然后更新他们的next指针
'''

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        queue = [[root]]
        while queue != []:
            node = queue.pop(0)
            tmp = []
            if len(node) > 1:               
                for u in range(len(node)-1):
                    node[u].next = node[u+1]
            for v in node:
                if v.left:
                    tmp.append(v.left)
                if v.right:
                    tmp.append(v.right)
            if tmp != []:
                queue.append(tmp)
  
'''
别人的：时间复杂度O(logn) 空间复杂度O(1)
利用两个指针: pre指针表示遍历层的上一层第一个节点，初始值为root
            cur指针表示遍历层的指针，初始值为None
    外循环就是pre = pre.left
    每一次外循环时：cur = pre
    当cur非空，就说明cur的左右子节点非空，
    就要设置next指针cur.left.next = cur.right
    这时候还要有一个判断：判断cur的next指针是否非空
    如果非空的话：cur.right.next = cur.next.left
    然后再进行内部循环　cur = cur.next
'''      
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        pre = root
        cur = None
        while pre.left:
            cur = pre
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
        