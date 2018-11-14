# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 07:57:18 2018

@author: xiaohong
"""

'''
快乐数
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。
如果可以变为 1，那么这个数就是快乐数。

输入: 19
输出: true
解释: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

'''
我的 0.99
'''

def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        
        squareSum = {}
        stop = False
        ishap = False
        while not stop:
            nsum = 0
            while n > 0 :
                nsum += (n % 10) ** 2
                n = n // 10                
            if nsum == 1:
                stop = True
                ishap = True
            if nsum in squareSum:
                stop = True
            else:
                squareSum[nsum]=True
                n = nsum                
        return ishap
    

'''
第二次做：　时间复杂度O(n) 空间复杂度O(1)
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        stop = False
        while True:
            tmp = 0
            while n > 0:
                tmp += (n % 10)**2
                n = n // 10
            n = tmp
            if n == 1:
                return True
            else:
                if n in res:
                    return False
                else:
                    res.append(n)