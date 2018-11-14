# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:25:13 2018

@author: xiaohong
"""

'''
最后一个单词长度
'''

'''
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:
输入: "Hello World"
输出: 5


'''

'''
我的 24ms best!
'''
def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """

        if s == '':
            return 0
        i = 0
        j = 0
        for k in s[::-1]:
            if s[-1-j] == ' ':
                j += 1
                i += 1
            else:
                j += 1
            
            if j>=len(s):
                break
            elif j > i and s[-1-j] == ' ':
                break
        return j - i
    
    
    