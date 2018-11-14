#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 19:40:44 2018

@author: pineapple
"""
'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
'''


'''
别人的: 时间复杂度O(n) 空间复杂度O(1)
思路：计算链表长度，如果k大于链表长度，需要取模
    设置快指针fast和慢指针slow，快指针先走k步
    然后快慢指针一起往前走，直到快指针到达末尾
    然后将快指针的next指向链表的head
    然后将慢指针的next节点设置为链表的新头
    然后将慢指针的next指向None

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 边界条件
        if k == 0  or not head:
            return head
        # 计算链表长度
        cur = head
        listlen = 0
        while cur:
            listlen += 1
            cur = cur.next
        # 如果k大于链表长度，需要取模
        k = k % listlen
        # 设置快指针fast和慢指针slow
        # 快指针先走k步
        slow = head
        fast = head
        i = 0
        while i < k:
            i += 1
            fast = fast.next
        # 然后快慢指针一起往前走，直到快指针到达末尾
        while fast.next:
            slow = slow.next
            fast = fast.next
        # 然后将快指针的next指向链表的head
        # 然后将慢指针的next节点设置为链表的新头
        # 然后将慢指针的next指向None
        fast.next = head
        newhead = slow.next
        slow.next = None
        return newhead