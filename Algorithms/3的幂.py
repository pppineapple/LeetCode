# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:16:55 2018

@author: xiaohong
"""

'''
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:
输入: 27
输出: true

示例 2:
输入: 0
输出: false

示例 3:
输入: 9
输出: true

示例 4:
输入: 45
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？
'''


'''
我的 0.34
思路， 递归
'''

def isPowerOfThree(n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 3 or n == 1:
            return True
        elif n < 3:
            return False
        else:
            if n == round(n**0.5, 2)**2:
                n = n ** 0.5
                return isPowerOfThree(n)
            else:
                if n % 3 == 0:
                    n = n // 3
                    return isPowerOfThree(n)
                else:
                    return False
                

