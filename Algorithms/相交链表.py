#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:10:20 2018

@author: pineapple
"""

'''
编写一个程序，找到两个单链表相交的起始节点。

 

例如，下面的两个链表：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
在节点 c1 开始相交。

 

注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        '''
   思路是这样的（题目中假设没有环）： 
1.分别遍历两个链表，如果尾节点不同则不相交，返回None，如果尾节点相同则求相交结点。 
2.求相交结点的方法是，求出链表长度的差值，长链表的指针先想后移动lenA-lenB。然后两个链表一起往后走，若结点相同则第一个相交点。 
3.求链表的长度，在遍历的时候就计算，并将每个结点放在字典中。 
        '''
'''
别人 250 ms
'''        
        heada = headA
        headb = headB
        Alen, Blen = 0, 0
        while heada:
            heada = heada.next
            Alen += 1
        while headb:
            headb = headb.next
            Blen += 1

        if heada != headb:
            return None
        
        heada = headA
        headb = headB
        if Alen > Blen:
            diff = Alen-Blen
            while diff > 0:
                heada = heada.next
                diff -= 1
        if Alen < Blen:
            diff = Blen-Alen
            while diff > 0:
                headb = headb.next
                diff -= 1
                
        while heada != headb:
            heada = heada.next
            headb = headb.next
        
        return heada

'''
第二次做
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return         
        lena = 0
        cura = headA
        while cura.next:
            lena += 1
            cura = cura.next
        lena += 1
        
        lenb = 0
        curb = headB
        while curb.next:
            lenb += 1
            curb = curb.next
        lenb += 1
        
        if cura != curb:
            return 
        
        i = 0
        cura = headA
        curb = headB
        if lena > lenb:            
            while i < lena - lenb:
                cura = cura.next
                i += 1
        if lenb > lena:
            while i < lenb - lena:
                curb = curb.next
                i += 1
        while cura != curb:
            cura = cura.next
            curb = curb.next
        return cura
    
    
'''
第三次做
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """      
        lenA = 0
        curA = headA
        while curA:
            lenA += 1
            curA = curA.next       
        lenB = 0
        curB = headB
        while curB:
            lenB += 1
            curB = curB.next        
        i = 0
        curA = headA
        curB = headB
        if lenA < lenB:
            curB = headB
            while i < lenB - lenA:
                curB = curB.next
                i += 1
        else:
            curA = headA
            while i < lenA - lenB:
                curA = curA.next
                i += 1
        while curA != curB:
            curA = curA.next
            curB = curB.next
        return curA
            