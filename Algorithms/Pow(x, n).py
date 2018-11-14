#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:22:57 2018

@author: pineapple
"""

'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
'''

'''
别人的：时间复杂度O(logn) 空间复杂度O(logn)
思路：直接就是递归，然后x*x，同时幂指数n/2
    递归出口是n==0返回1.0, 
    注意中间递归时，如果n % 2 == 1，那么要取出一个x与结果相乘，因为n/2
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        elif n < 0:
            return self.myPow(1/x, -n)
        else:
            if n % 2 == 1:
                return self.myPow(x*x, n/2) * x
            else:
                return self.myPow(x*x, n/2)