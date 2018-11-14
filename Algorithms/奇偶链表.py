#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:00:20 2018

@author: pineapple
"""

'''
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，
而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，
时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL 
输出: 2->3->6->7->1->5->4->NULL
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
'''

'''
我的：时间复杂度O(n) 空间复杂度O(1)
思路：双指针，建立odd和even表示奇数和偶数位置的node
    每次循环，两个指针都是移动两个节点
    循环出口是odd的下一个节点为None或者even的下一个节点为None
    但要注意的是：在while语句中，odd.next必须放在even.next前面
    循环结束后，再将odd的next指针指向偶数链表的头evenhead
    返回head
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        odd = head
        evenhead = head.next
        even = evenhead
        if not even or not even.next:
            return head
        while odd.next and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        odd.next = evenhead
        return head
        