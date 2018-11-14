# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:24:41 2018

@author: xiaohong
"""

'''
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。
'''

'''
我的 0.98
思路： 短除法, 用栈保存余数，然后反序输出，注意考虑边界0
'''

def convertToBase7(num):
        """
        :type num: int
        :rtype: str
        """
        
        if num >= 0:
            posi = True
        else:
            posi = False
            
        num = abs(num)
        stack = []
        while num > 0:
            res = num % 7
            num = num // 7
            stack.append(res)
            
        if posi:
            return ''.join(map(str,stack[::-1]))
        else:
            return '-' + ''.join(map(str,stack[::-1]))
        
convertToBase7(1)
