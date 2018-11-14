# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:49:56 2018

@author: xiaohong
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        while head != None and head.val == val:
            head = head.next
        
        if head == None:
            return head
        
        cur = head
        while cur:
            if cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
            
            
            



