#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 10:36:06 2018

@author: pineapple
"""

'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''

'''
我的: 时间复杂度O(nlogn) 空间复杂度O(n)
思路：参考找质数的方法：厄拉多塞筛法(Sieve of Eeatosthese)。
    这里只需要计算质数个数
    将不是质数的元素改写为０
    对质数中不为０元素求和
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = range(2,n)
        i = 2
        while i ** 2 < n:
            for j in range(i-2, len(res), i):
                if res[j] != i:
                    res[j] = 0
            i += 1
        
        return sum([1 for u in res if u != 0 ])
