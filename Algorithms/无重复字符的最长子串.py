#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:31:33 2018

@author: pineapple
"""
'''
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 无重复字符的最长子串是 "abc"，其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 无重复字符的最长子串是 "b"，其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 无重复字符的最长子串是 "wke"，其长度为 3。
     请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。
'''

'''
我的：时间复杂度O(n) 空间复杂度O(1)
思路：使用双指针移动，循环出口为慢指针left=len(s)
    用一个变量max_sublen来统计虽大的连续不重复子串长度 
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_sublen = 0 
        left = 0
        right = 1
        
        while left < len(s):
            sub = set(s[left:right])
            if len(sub) == right-left:
                max_sublen = max(max_sublen, len(sub))
                right += 1
            else:
                left += 1
                
        return max_sublen
    
s = "aab"
s = "pwwkew"
s = "dvdf"
S = Solution()
S.lengthOfLongestSubstring(s)
