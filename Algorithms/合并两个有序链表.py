# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 17:44:35 2018

@author: xiaohong
"""

'''
合并两个有序链表
'''

'''
将两个有序链表合并为一个新的有序链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
参考别人 32ms
'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        mergeListNode = ListNode(0)
        merge = mergeListNode
        
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                merge.next = l2
                l2 = l2.next
            else:
                merge.next = l1
                l1 = l1.next
            merge = merge.next
            
        if l1 is None:
            merge.next = l2
        if l2 is None:
            merge.next = l1
        
        return mergeListNode.next
    
'''
我的：
思路差不多，比较l1和l2的节点值的大小，然后移动值小的那个链表的
'''
        
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        
        head = ListNode(0)
        cur = head
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    tmp = ListNode(l1.val)
                    l1 = l1.next
                else:
                    tmp = ListNode(l2.val)
                    l2 = l2.next
            elif l1:
                tmp = ListNode(l1.val)
                l1 = l1.next
            elif l2:
                tmp = ListNode(l2.val)
                l2 = l2.next
            cur.next = tmp
            cur = cur.next
        return head.next
'''
第三次做
'''
    
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newhead = ListNode(0)
        cur = newhead
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next    
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return newhead.next