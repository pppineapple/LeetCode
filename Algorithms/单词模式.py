# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:34:16 2018

@author: xiaohong
"""
'''
单词模式
'''

'''
给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
这里的遵循指完全匹配，
例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false

示例 3:
输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false

示例 4:
输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
'''


'''
别人的 0.98 
思路： 建立两个字典，根据映射值是否相等来判断
'''

def wordPattern(pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        strlist = str.split(' ')
        patdict = {}
        strdict = {}
        
        if len(pattern) != len(strlist):
            return False
        for i in range(len(pattern)):
            if patdict.get(pattern[i]) != strdict.get(strlist[i]):
                return False
            patdict[pattern[i]] = i
            strdict[strlist[i]] = i
        return True