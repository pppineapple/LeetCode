# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 08:23:57 2018

@author: xiaohong
"""


'''

对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False


示例：
输入: 28
输出: True
解释: 28 = 1 + 2 + 4 + 7 + 14
'''

'''
别人的 1
思路： 从2开始找出num的因子树，然后用num减去num的因子数，一直到num的开根号，
因为开根号之后的数字实际上是之前的重复
'''
def checkPerfectNumber(num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 6:
            return False
        temp = num - 1
        for i in range(2, int(num**0.5+1)):
            if num % i == 0:
                temp = temp - i - num//i
        if (num**0.5)**2 == num:
            temp = temp + num**0.5
        
        return temp == 0


28**0.5

