#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 08:42:16 2018

@author: pineapple
"""


'''
反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。
'''

'''
我的　时间复杂度O(n) 空间复杂度O(n)
思路：　双指针对撞 
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuan = 'aeiouAEIOU'
        slist = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            if slist[left] in yuan and slist[right] in yuan:
                tmp = slist[left]
                slist[left] = slist[right]
                slist[right] = tmp
                left += 1
                right -= 1
            elif slist[left] in yuan:
                right -= 1
            elif slist[right] in yuan:
                left += 1
            else:
                right -= 1
                left += 1
        return ''.join(slist)
    
    
'''
更简洁的代码
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuan = 'aeiouAEIOU'
        slist = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            if slist[left] not in yuan:
                left += 1
                continue
            if slist[right] not in yuan:
                right -= 1
                continue
            if left < right:
                tmp = slist[left]
                slist[left] = slist[right]
                slist[right] = tmp
            left += 1
            right -= 1
        return ''.join(slist)

