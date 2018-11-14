#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:04:04 2018

@author: pineapple
"""
'''
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1
'''

'''
别人的, 考察的是二进制还有符号运算 ^ & | ~
'''

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
            print carry, a, b
        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)


a = 1823
b = 3241
s = Solution()
s.getSum(a,b)


