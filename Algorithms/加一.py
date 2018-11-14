# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 08:17:01 2018

@author: xiaohong
"""

'''
给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
'''


'''
我的 1 best
思路：递归， 边界条件是 数字加一大于零
'''

def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """       
        
        if digits[-1] + 1 < 10:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            if len(digits) == 1:
                digits[-1] = 0
                digits.insert(0, 1)
                return digits
            else:
                digits[-1] = 0
                sub = plusOne(digits[:-1])
                sub.append(digits[-1])
                return sub
            
digits = [9,9]
plusOne(digits)

digits = [9]


'''
第二次做
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tmp = digits[-1] + 1
        if tmp <= 9:
            digits[-1] = tmp
            return digits
        else:
            digits[-1] = 0
            tmp = 1
            for i in range(len(digits)-2, -1 ,-1):
                digits[i] += tmp
                if digits[i] > 9:
                    tmp = 1
                    digits[i] = 0
                else:
                    tmp = 0
                    break
            if tmp == 1:
                digits.insert(0,1)
            return digits