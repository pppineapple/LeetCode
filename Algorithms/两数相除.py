#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:12:35 2018

@author: pineapple
"""
'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，
要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。
本题中，如果除法结果溢出，则返回 231 − 1。
'''


'''
我的：　时间复杂度O(logn) 空间复杂度O(1)
思路：除数和被除数应该是在x**0.5的左右两边的，或者都是x**0.5
    确定好余数的区间就可以二分查找了
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend * divisor > 0:
            flag = 1
            dividend = abs(dividend)
            divisor = abs(divisor)
        else:
            flag = -1
            dividend = abs(dividend)
            divisor = abs(divisor)
        
        if divisor > dividend ** 0.5:
            left = 1
            right = int(dividend ** 0.5)
        else:
            left = int(dividend ** 0.5)
            right = dividend
        found = False
        while left <= right and not found:
            mid = (left+right)//2
            if mid * divisor == dividend:
                found = True
            elif mid * divisor > dividend:
                right = mid - 1
            elif mid * divisor < dividend:
                left = mid + 1
        if found:
            ans = mid*flag
        else:
            ans = right*flag
        
        if ans < -2**31 or ans > 2**31-1:
            return 2**31-1
        else:
            return ans

dividend =2147483647
divisor = 2
s = Solution()
s.divide(dividend,divisor)
