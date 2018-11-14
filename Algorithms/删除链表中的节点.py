# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:34:22 2018

@author: xiaohong
"""


'''
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:
    4 -> 5 -> 1 -> 9

示例 1:
输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2:
输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
说明:
链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。
'''

'''
别人的 1 
解题思路：通常情况下，如果告诉你head和val,那就一步一步找到链表中val和给出val相同的节点，然后
把上一个节点的指针知道下下个节点中去
但是这个题直接告诉你节点node了，所以直接把这个节点的val复制为下一个node的val,然后将这个node
的指针指向下下node,相当于把下一个node复制到给出的这个node上，然后把下一个node删除。
'''




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val = node.next.val
        node.next = node.next.next
        
'''
第二次做，还是没做出来,看了思路
'''
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val = node.next.val
        node.next = node.next.next