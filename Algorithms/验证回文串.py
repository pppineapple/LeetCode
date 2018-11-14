#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 22:25:14 2018

@author: pineapple
"""
'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，
可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
'''

'''
我的思路：　时间复杂度O(n) 空间复杂度O(1)
双指针对撞，先把s全部变成只有字符和数字的
然后指针对撞 
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        alph = 'abcdefghijklmnopqrstuvwxyz0123456789'
        shorts = ''
        for i in s:
            if i.lower() in alph:
                shorts += i.lower()
        left = 0
        right = len(shorts)-1
        
        while left < right:
            if  shorts[left] != shorts[right]:
                return False
            left += 1
            right -= 1
        return True
    
    
'''
更简洁的代码
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        left = 0
        right = len(s)-1
        while left < right:
            # Python isalnum() 方法检测字符串是否由字母和数字组成
            if s[left].isalnum() == False:
                left += 1
                continue
            if s[right].isalnum() == False:
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
        
'''
第三次做　
'''
        
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        alph = 'abcdefghijklmnopqrstuvwxyz0123456789'
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].lower() in alph and s[right].lower() in alph:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
            elif s[left].lower() not in alph:
                left += 1
            elif s[right].lower() not in alph:
                right -= 1
            else:
                left += 1
                right -= 1
        return True