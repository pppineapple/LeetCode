# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 19:53:10 2018

@author: xiaohong
"""

'''
实现 strStr() 函数。
'''

'''
给定一个 haystack 字符串和一个 needle 字符串，
在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。
'''


'''
别人的 44ms
'''
def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle == '':
            return 0
        j = 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                j = 1
                while j<len(needle) and haystack[i+j] == needle[j]:
                    j += 1
                if j==len(needle):
                    return i
        return -1
 
'''
best 24ms
'''               
def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == '':
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1
    
    
'''
第二次做　时间复杂度O(nk) 空间复杂度O(1)
思路：滑块移动法
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        k = len(needle)
        i = 0
        while i <= len(haystack) - k:
            if haystack[i:i+k] == needle:
                return i
            i += 1
        return -1