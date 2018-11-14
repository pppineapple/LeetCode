# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 08:34:47 2018

@author: xiaohong
"""

'''
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，
它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。
'''

'''
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''

 # Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            output = ListNode(0)
            output_last = output
            carry = 0
            while l1 or l2:
                sum_l = 0
                if l1:
                    sum_l += l1.val
                    l1 = l1.next
                if l2:
                    sum_l += l2.val
                    l2 = l2.next
                sum_l += carry
                carry = sum_l // 10
                output_last.next = ListNode(sum_l % 10)
                output_last = output_last.next
            if carry >= 1:
                output_last.next = ListNode(1)
            output_last = output.next
            del output
            return output_last
            
l1_1 = ListNode(2)
l1_1.next = ListNode(4)
print l1_1.val, l1_1.next
l1_2 = l1_1.next
print l1_2.val, l1_2.next
l1_2.next = ListNode(3)
print l1_2.val, l1_2.next
l1_3 = l1_2.next
print l1_3

l1 = ListNode(2)
l1.next = l11 = ListNode(4)
l11.next = l12 = ListNode(3)
l1.val
l1.next.val
l1.next.next.val
l1.next.next.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1_1 = l1.next
l1_1.next = ListNode(3)
l1_1_1 = l1_1.next
l1_1_1.val

l2 = ListNode(5)
l2.next = ListNode(6)
l2_1 = l2.next
l2_1.next = ListNode(4)
l2_1_1 = l2_1.next
l2_1_1.val
l2.val
l2_1.val
l2_1_1.val

s = Solution()
a = s.addTwoNumbers(l1,l2)
print a.val, a.next.val, a.next.next.val

'''
我的：
思路：同时遍历两个链表，对应位置相加，如果某各链表到尾部了，就只加另一个链表的值
    用一个变量carry记录进１的情况，主要，遍历两个链表完成时也要看一下carry的值
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        header = ListNode(0)
        cur = header
        while l1 or l2:
            if l1 and l2:
                numl1 = l1.val
                numl2 = l2.val
                l1 = l1.next
                l2 = l2.next
                numsum = numl1 + numl2 + carry
            elif l1:
                numsum = l1.val + carry
                l1 = l1.next
            elif l2:
                numsum = l2.val + carry
                l2 = l2.next
            if numsum >= 10:
                carry = 1
                numsum = numsum % 10
            else:
                carry = 0
            tmp = ListNode(numsum)
            cur.next = tmp
            cur = cur.next
            
        if carry > 0:
            cur.next = ListNode(1)
        return header.next
 
    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new = ListNode(0)
        ans = new
        carry = 0
        while l1 or l2:
            tmp = carry
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            if tmp >= 10:
                tmp = tmp % 10
                carry = 1
            else:
                carry = 0
            ans.next = ListNode(tmp)
            ans = ans.next
        if carry > 0:
            ans.next = ListNode(1)
            ans = ans.next
            
        return new.next