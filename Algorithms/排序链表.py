#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 10:41:49 2018

@author: pineapple
"""



'''
我的：时间复杂度O(nlogn) 空间复杂度O(n)
思路：　将链表值全部放到数组里面，对数组排序
    再根据数组，将链表写出来
    这是一种取巧的办法，并没有走出题的思路
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        cur = head
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next
        nums.sort()
        newhead = ListNode(nums[0])
        cur = newhead
        for i in range(1,len(nums)):
            cur.next = ListNode(nums[i])
            cur = cur.next
        return newhead
    
    
'''
别人的：　时间复杂度O(nlogn) 空间复杂度O(1)
思路：考虑排序：这就需要分析一下各个排序算法的复杂度了。
时间复杂度在O(nlogN)的排序算法是快速排序，堆排序，归并排序。
但是快排的最坏时间复杂度是O(n^2),平均时间复杂度为O(nlogn)，所以不考虑快速排序。
而堆排序太繁琐了。。。。。emmm。。。生硬地排除了。
对于数组来说占用的空间复杂度为O(1),O(n),O(n)。
但是对于链表来说使用归并排序占用空间为O(1).

所以采取归并的思想：将链表递归从中间切割开，切的时候要写一个方法来找到链表中点。
就是快慢指针法，快指针走两步，慢指针走一步，快指针走到头，慢指针即为中点。
然后采用合并两个有序链表的方法递归合并两个相邻的子链表。

'''
    
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        split = self.get_mid(head)
        headA = head
        headB = split.next
        split.next = None
        return self.mergeTwoList(self.sortList(headA), self.sortList(headB))
        
        
    def get_mid(self, head):
        if not head:
            return head
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def mergeTwoList(self, headA, headB):
        newhead = ListNode(0)
        cur = newhead
        while headA or headB:
            if headA and headB:
                if headA.val < headB.val:
                    tmp = headA
                    headA = headA.next
                else:
                    tmp = headB
                    headB = headB.next
            elif headA:
                tmp = headA
                headA = headA.next
            elif headB:
                tmp = headB
                headB = headB.next
                
            cur.next = tmp
            cur = cur.next
        return newhead.next

'''
第二遍
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        A = head
        B = slow.next
        slow.next = None
        headA = self.sortList(A)
        headB = self.sortList(B)
        ans = self.merge(headA, headB)
        return ans
     
    def merge(self, headA, headB):
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