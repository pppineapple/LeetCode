# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 20:26:59 2018

@author: xiaohong
"""

'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2

示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
'''

'''
我的 36 ms
'''


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head        
        node = head
        while node.next != None:
            nodeNext = node.next
            if node.val == nodeNext.val:
                node.next = nodeNext.next
#                node = node.next
            else:
                node = nodeNext                
        return head
    
a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(2)    
a.next.next.next =ListNode(3)    
a.next.next.next.next = ListNode(3)    


head = a
node.next.val
nodeNext
node.next.val
nodeNext.val
node.val
    
    