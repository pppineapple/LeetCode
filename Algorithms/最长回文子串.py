#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:13:43 2018

@author: pineapple
"""

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''

'''
别人的：时间复杂度O(n^2) 空间复杂度O(1)
思路：
回文有奇回文和偶回文，abcba是奇回文，abccba是偶回文
回文都是中心对称，找到对称点后，同时向前后寻找回文的最长串即可
奇回文和偶回文可以归为同一种情况，即abcba以c为对称点，abccba以cc为对称点，

外循环值直接遍历s的长度len(s)
然后将s[i]这个值单做奇回文的中心点，向两边扩展，看两边的值是否相等，
相等就是回文串，然后继续向两边扩展，然后记录最长的子回文串
别急，在本次循环中，还要判断一下偶回文的情况，将s[i:i+2]作为偶回文串的中心，
向两边扩展，记录最长子回文串。
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        maxlen = 0
        maxstr = ''
        for i in range(len(s)):
            # 奇回文
            left1 = i-1
            right1 = i+1
            while left1 >= 0 and right1 < len(s):
                if s[left1] == s[right1]:
                    left1 -= 1
                    right1 += 1
                else:
                    break
            if right1 - left1 + 1 > maxlen:
                maxlen = right1 - left1 + 1
                maxstr = s[left1+1:right1]
            #　偶回文
            left2 = i
            right2 = i+1
            while left2 >=0 and right2 < len(s):
                if s[left2] == s[right2]:
                    left2 -= 1
                    right2 += 1
                else:
                    break
            if right2 - left2 + 1 > maxlen:
                maxlen = right2 - left2 + 1
                maxstr = s[left2+1:right2]
        
        return maxstr
 
'''
更简洁的代码
'''
class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        if len(s) < 2:
            return s
        for i in range(len(s)):
            left1 = i
            right1 = i
            while left1 >=0 and right1 < len(s) and s[left1] == s[right1]:
                left1 -= 1
                right1 += 1
            if maxlen < right1 - left1 + 1:
                maxlen = right1 - left1 + 1
                retstr = s[left1+1:right1]
            left2 = i
            right2 = i+1
            while left2 >= 0 and right2 < len(s) and s[left2] == s[right2]:
                left2 -= 1
                right2 += 1
            if maxlen < right2 - left2 + 1:
                maxlen = right2 - left2 + 1
                retstr = s[left2+1:right2]
        return retstr    


s = 'babad' 
s = 'ac'   
s = 'ccc'
s = 'aaaa'
S =Solution()
S.longestPalindrome(s)    

'''
第二次做
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        point = 0
        max_len = 1
        max_len_sub = s[point]
        while point < len(s)-1:
            #奇数中心对称
            left1 = point - 1
            right1 = point + 1
            while left1 >= 0 and right1 <= len(s)-1:
                if s[left1] == s[right1]:
                    if right1-left1+1 >= max_len:
                        max_len = right1-left1+1
                        max_len_sub = s[left1:right1+1]
                    left1 -= 1
                    right1 += 1
                else:
                    break
            left2 = point
            right2 = point+1
            while left2 >= 0 and right2 <= len(s)-1:
                if s[left2] == s[right2]:
                    if right2-left2+1 >= max_len:
                        max_len = right2-left2+1
                        max_len_sub = s[left2:right2+1]
                    left2 -= 1
                    right2 += 1
                else:
                    break
            point += 1
        return max_len_sub