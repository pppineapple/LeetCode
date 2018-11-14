#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 10:55:43 2018

@author: pineapple
"""

'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，
同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
'''

'''
我的：时间复杂度O(n^2) 空间复杂度O(n)
思路：将字符串按照空格切分成列表
    然后遍历列表，对每个字符串反转(双指针对撞)
    然后每次反转完将结果保持到新的结果列表里面
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.split(' ')
        output = []
        for s in slist:
            s_list = list(s)
            left = 0
            right = len(s) - 1
            while left < right:
                tmp = s_list[left]
                s_list[left] = s_list[right]
                s_list[right] = tmp
                right -= 1
                left += 1
            output.append(''.join(s_list))
        return ' '.join(output)
    
'''
更加pythonioc的写法
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.split(' ')
        output = []
        for s in slist:
            s = s[::-1]
            output.append(s)
        return ' '.join(output)