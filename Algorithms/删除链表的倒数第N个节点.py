#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 10:50:34 2018

@author: pineapple
"""

'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
'''

'''
别人的：时间复杂度O(n) 空间复杂度O(1)
思路：快慢两个指针slow和fast在head位置
    先让快指针fast移动到n+1的位置处
    然后让fast和slow一起移动，直到fast移动到链表末端
    将slow的next指针指向slow.next.next
需要注意的是：因为可能会遇到删除head节点的情况
    所以需要在head前面建立一个新的节点newhead
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        newhead = ListNode(0)
        newhead.next = head
        slow = newhead
        fast = newhead
        i = 0
        while i < n + 1 :
            fast = fast.next
            i += 1            
        while fast:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        return newhead.next
    
'''
别人的：时间复杂度O(n)　空间复杂度O(n)
思路：直接将目标位置的前面位置节点的值直接替换到目标位置节点上，
    然后往前继续该操作，最后返回head.next
    这里写了一个辅助函数getindex用来递归从尾部开始查找链表的索引，
    即最后的位置的index = 1,如果该位置的索引大于n了，就要更改该
    位置的值，
'''
class Solution1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        self.getindex(head, n)
        return head.next
               
    def getindex(self, node, n):
        if not node:
            return 0
        index = self.getindex(node.next, n) + 1
        if index > n:
            node.next.val = node.val
        return index