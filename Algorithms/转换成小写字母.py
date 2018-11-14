# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:11:20 2018

@author: xiaohong
"""

'''
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，
并将该字符串中的大写字母转换成小写字母，之后返回新的字符串

示例 1：
输入: "Hello"
输出: "hello"

示例 2：
输入: "here"
输出: "here"

示例 3：
输入: "LOVELY"
输出: "lovely"
'''

def toLowerCase(str):
        """
        :type str: str
        :rtype: str
        """
        
        lowerChar = 'abcdefghijklmnopkrstuvwsyz'
        upperChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        outputStr = ''
        for s in str:
            if s in upperChar:
                outputStr = outputStr + lowerChar[upperChar.index(s)]
            else:
                outputStr = outputStr + s
        return outputStr
    
toLowerCase('Hello')
toLowerCase('here')
toLowerCase('LOVELY')
