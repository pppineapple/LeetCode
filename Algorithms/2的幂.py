# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 10:03:13 2018

@author: xiaohong
"""

'''
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
输入: 1
输出: true
解释: 20 = 1

示例 2:
输入: 16
输出: true
解释: 24 = 16

示例 3:
输入: 218
输出: false
'''

'''
我的 0.98
思路 递归
'''

def isPowerOfTwo(n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 3 or n == 0:
            return False
        elif n == 2 or n == 1:
            return True
        else:
            rem = n % 2
            n = n // 2
            if rem > 0:
                return False
            else:
                return isPowerOfTwo(n)
                
isPowerOfTwo(9)


'''
第二次做；我的：　时间复杂度O(n) 空间复杂度O(1)
思路：　对n进行除２处理，如果余数不为０，返回False
        循环出口条件是：ｎ <= ２
        最后判断一下，循环之后的n是否为２
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        while n > 2:
            res = n % 2
            if res != 0:
                return False
            n = n // 2
        if n == 2:
            return True
        else:
            return False