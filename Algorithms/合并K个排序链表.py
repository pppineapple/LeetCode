#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 10:55:51 2018

@author: pineapple
"""

'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''

'''
别人的：　时间复杂度O(max(nk, nlogn)) 空间复杂度O(n)
思路：直接遍历所有的链表，将值放进一个新的数组
    然后对数组排序，最后根据排序好的数组进行链表创建
    注意边界条件。
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) < 1:
            return None
        elif sum([1 if i else 0 for i in lists]) == 0:
            return lists[0]
        
        res = []
        for l in lists:
            while l:
                res.append(l.val)
                l = l.next
        res.sort()
        head = ListNode(res[0])
        cur = head
        for r in range(1,len(res)):
            tmp = ListNode(res[r])
            cur.next = tmp
            cur = cur.next
        return head

'''
别人的：时间复杂度O(nklogk)，空间复杂度O(1)
思路：直接对链表列表中的链表两两合并，合并方法用合并两个有序数组的方法
    新建一个变量tmp，用来存储每一次两两合并之后的链表
    然后将tmp赋值给lists，即lists = tmp
    直到lists的长度为１，返回lists[0]
'''    
    
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) < 1:
            return None
        elif sum([1 if i else 0 for i in lists]) == 0:
            return lists[0]
        
        while len(lists) > 1:
            tmp = []
            for i in range(0, len(lists)-1, 2):
                l = self.mergeTwoLists(lists[i], lists[i+1])
                tmp.append(l)
            if len(lists) % 2 == 1:
                tmp.append(lists[-1])
            lists = tmp
        return lists[0]
    
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
第二次做：
'''
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        while len(lists)>1:
            tmp = []
            for i in range(0, len(lists)-1, 2):
                new = self.mergeTwoLists(lists[i], lists[i+1])
                tmp.append(new)
            if len(lists) % 2 == 1:
                tmp.append(lists[-1])
            lists = tmp
        return lists[0]
    
    def mergeTwoLists(self, headA, headB):
        headtmp = ListNode(0)
        cur = headtmp
        while headA and headB:
            if headA.val < headB.val:
                cur.next = headA
                headA = headA.next
            else:
                cur.next = headB
                headB = headB.next
            cur = cur.next
        if headA:
            cur.next = headA
        if headB:
            cur.next = headB
        return headtmp.next