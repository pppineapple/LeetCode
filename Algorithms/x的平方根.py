# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 14:05:26 2018

@author: xiaohong
"""


'''
x 的平方根

实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
由于返回类型是整数，小数部分将被舍去。
'''

'''
别人的代码 40ms
'''

def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        min = 0
        max = x
        while max - min > 1:
            mid = (min+max)//2
            if x > mid * mid:
                min = mid
            elif x < mid * mid:
                max = mid
            else:
                return mid
        return min

mySqrt(10)

'''
第二次做：　时间复杂度O(logn),空间复杂度O(1)
思路：二分法，将问题看做是在递增序列[1,2,3,...,x]上
    找到一个数i,这个数i必须满足i^2不大于target =ｘ,并且(i+1)^2>target=x
    
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 1
        right = x
        while left <= right:
            mid = (left+right)//2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                right = mid - 1
            elif mid ** 2 < x:
                left = mid + 1
        return right
        