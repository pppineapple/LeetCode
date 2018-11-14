# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:09:59 2018

@author: xiaohong
"""

'''
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

示例 :
输入: 11
输出: 3
解释: 整数 11 的二进制表示为 00000000000000000000000000001011
 

示例 2:
输入: 128
输出: 1
解释: 整数 128 的二进制表示为 00000000000000000000000010000000
'''

'''
我的 0.98 思路：转化为二进制的步骤，然后将余数相加
'''

def hammingWeight(n):
        """
        :type n: int
        :rtype: int
        """
        rem = 0
        while n > 0:
            rem += n % 2
            n = n // 2
            
        return rem
    
'''
第二次做
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = ''
        while n > 0:
            res = n % 2
            n = n//2
            ans = str(res) + ans
        return ans.count('1')
        