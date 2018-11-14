# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:22:34 2018

@author: xiaohong
"""

'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''

'''
别人的 0.97
思路： 先用快慢双指针，快指针跑到最后，慢指针跑到中间，然后从慢指针出将后半部分链表翻转
      在逐一与前半部分的链表比较
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head == None or head.next == None:
            return True
        
        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        curr = slow
        if not curr.next:
            right = curr
        else:
            while curr.next:
                temp = ListNode(curr.next.val)
                temp.next = slow
                curr.next = curr.next.next
                slow = temp
            right = temp 
        
        left = head
        while right:
            if left.val != right.val:
                return False
            else:
                left = left.next
                right = right.next
        return True
    
'''
第二次做, 别人的，时间复杂度O(n) 空间复杂度O(1)
思路：先通过快慢指针找到链表中点，然后反转后半部分链表和前面的链表比较
    如果是奇数项，slow的位置就是中心的奇数项
    如果是偶数项，slow的位置就是中心两个位置的左边一个位置
    所以后半部分需要反转的链表的头部是slow.next
    
    然后编写一个辅助函数翻转后半部分链表
    然后遍历翻转之后的链表，如果值不相同了，就返回False

'''

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        index = slow.next
        slow = self.reverse(index)
        print slow.val
       
        while slow:
            if head.val == slow.val:
                head = head.next
                slow = slow.next
            else:
                return False
        return True
    
    def reverse(self, head):
        if not head:
            return head
        cur = head
        slow = head
        while cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = slow
            slow = tmp
        return slow