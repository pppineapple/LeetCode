#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 12:02:02 2018

@author: pineapple
"""
'''
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的深度拷贝。 
'''


'''
别人的思路：时间复杂度O(n), 空间复杂度O(n)
思路：链表复制分为两步：
    1.复制链表的值
    2.复制链表的指针
    这里先把链表的值存放到hash表中
    然后第二遍遍历在赋值链表的指针关系
    注意：要手动在hash表中加入None:None的键值对关系，
        因为链表中存在None节点

'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        hash = {}
        node = head
        while node:
            hash[node] = RandomListNode(node.label)
            node = node.next
        hash[None] = None
        node = head
        while node:
            hash[node].next = hash[node.next]
            hash[node].random = hash[node.random]
            node = node.next
        return hash[head]