#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 20:53:32 2018

@author: pineapple
"""

'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

说明：不允许修改给定的链表。

进阶：
你是否可以不用额外空间解决此题？
'''

'''
别人的：　时间复杂度O(n^2) 空间复杂度O(1)
思路：

　　　　　环路周长L  －－－－*相遇点
          　　　　　|       |
                    |       |
    *－－－－－－－*－－－－ 起点到相遇点相距M
   head     K      起点 
   
那么我们有，快慢指针相遇时所走过的步数： 
step_slow = K + M 
step_faster = K + M + n*L 
又因为快指针每次都多走一步： 
step_faster = 2 * step_slow 
由以上三个公式可以推断出 
K ＝ (n-1)L + L - M 
所以，当快慢指针在相遇点相遇时。
假设一个新的指针point从head开始往前走，慢指针也往前走，步长为１
那么当point走到起点时，慢指针也会到起点
即　point == slow时，该点为环形起点

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                point = head
                while point != slow:
                    point = point.next
                    slow = slow.next
                return point
        return 