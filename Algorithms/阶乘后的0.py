# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:58:49 2018

@author: xiaohong
"""

'''
给定一个整数 n，返回 n! 结果尾数中零的数量。
'''

'''
别人的 0.69
'''

def trailingZeroes(n):
        """
        :type n: int
        :rtype: int
        """
        output = 0
        while n > 5:
            n = n // 5
            output = output + n
            
        return output
        
trailingZeroes(13)        

range(10, 13, 10)
range(10, 233, 10)
