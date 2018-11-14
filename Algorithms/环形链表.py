# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:22:18 2018

@author: xiaohong
"""

'''
给定一个链表，判断链表中是否有环。

进阶：
你能否不使用额外空间解决此题？
'''

'''
额外空间法 我的 0.20
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = head
        val = {}
        found = False
        while a and not found:
            if id(a) not in val:
                val[id(a)] = True
                a = a.next
            else:
                found = True
        return found
            



'''
双指针法 0.77
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
            
'''
我的第二次:　双指针法
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = head.next
        while slow and fast:
            if slow == fast:
                return True
            else:
                if slow.next and fast.next and fast.next.next:
                    slow = slow.next
                    fast = fast.next.next
                else:
                    return False
        return False

'''
第三次做：　
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
                
        return False