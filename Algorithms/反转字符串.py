#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 10:49:12 2018

@author: pineapple
"""

'''
编写一个函数，其作用是将输入的字符串反转过来。

示例 1:

输入: "hello"
输出: "olleh"
示例 2:

输入: "A man, a plan, a canal: Panama"
输出: "amanaP :lanac a ,nalp a ,nam A"
'''

'''
我的：　时间复杂度O(n) 空间复杂度O(n)
思路：　双指针对撞，将字符串转化为列表，
        左右指针分别从列表首尾遍历，然后相互交换元素
        最后将反转的列表转为字符串
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            tmp = slist[left]
            slist[left] = slist[right]
            slist[right] = tmp
            left += 1
            right -= 1
        return ''.join(slist)