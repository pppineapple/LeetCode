# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:40:23 2018

@author: xiaohong
"""

'''
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:
输入: 38
输出: 2 
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
'''

'''
我的 0.97
思路： 计算num各位的和利用%10相加余数得到，然后就是递归计算，递归出口是num<10
'''

def addDigits(num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        else:
            res = 0
            while num > 0:
                res += num % 10
                num = num // 10
            num = res
            return addDigits(num)
        
addDigits(38)
