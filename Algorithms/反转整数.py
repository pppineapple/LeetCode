# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 12:00:50 2018

@author: xiaohong
"""

def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        num = '0123456789'
        x_list = list(str(x))
        x_rev = ''
        while len(x_list) > 1:
            x_rev = x_rev + x_list.pop()
        
        x_list_first = x_list.pop()
        if x_list_first not in num:
            x_rev = x_list_first + x_rev
        else:
            x_rev = x_rev + x_list_first
        
        output = int(x_rev)

        if output < 2 ** 31 - 1 and output > -2 ** 31:
            return output
        else:
            return 0

'''
第二次做：时间复杂度O(n),空间复杂度O(n)
思路：先用变量positive记录x的符号，然后对x取绝对值
    将x按位数倒着储存到数组xlist里面
    然后再从xlist尾部通过×１０法将颠倒的数字写出来
    然后再还原符号，比较数字是否超出范围[−2**31,  2**31 − 1]
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            positive = True
        elif x < 0:
            positive = False
        else:
            return 0
        xlist = []
        x = abs(x)
        while x > 0:
            res = x % 10
            x = x // 10
            xlist.append(res)
        result = 0
        i = 0
        while xlist != []:
            num = xlist.pop() * 10 ** i
            result += num
            i += 1
        if not positive:
            result = result * (-1)
        if result > 2**31-1 or result < -2**31:
            return 0
        else:
            return result