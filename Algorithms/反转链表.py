# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 20:28:28 2018

@author: xiaohong
"""

'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''

'''
我的 时间复杂度O(n) 空间复杂度O(1) 0.95
思路： 根据原顺序迭代构建新节点，然后将新节点指针指向当前节点，当前节点指针指向下下个节点
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        cur = head
        new = cur
        while cur.next:
            tmp = ListNode(cur.next.val)
            tmp.next = new
            new = tmp
            cur.next = cur.next.next
            
        return new

'''
我的:
'''            

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head        
        cur = head
        slow = cur
        while cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = slow
            slow = tmp
            
        return tmp
    
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        first = head
        cur = head
        tmp = head
        while first.next:
            cur = first.next
            first.next = cur.next
            cur.next = tmp
            tmp = cur
        return cur