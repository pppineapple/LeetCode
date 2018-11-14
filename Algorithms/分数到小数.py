#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 13:26:01 2018

@author: pineapple
"""

'''
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，
以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"
'''

'''
我的：时间复杂度O(n) 空间复杂度O(n)
思路：利用一个数组f表示小数位中整除分母得到的余数，
    利用a一个数组ns_f表示小数位中整除分母得到的商
    每次循环中，如果余数在数组中出现了,就说明这个分数是循环小数，结束循环
    并且ans_f数组中对应f数组中从该余数的位置起到数组f末端的元素都是循环部分
    每次循环中，如果余数变成了0，就说小数是不循环的，结束循环，
    并且小数部分就是ans_f整个数组
    注意判断符号
'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator * denominator > 0:
            flag = 1
            numerator = abs(numerator)
            denominator = abs(denominator)
        elif numerator * denominator <0:
            flag = -1
            numerator = abs(numerator)
            denominator = abs(denominator)
        else:
            return '0'
        
        f = []
        ans_f = []
        i = numerator // denominator
        res = numerator % denominator
        while res!=0 and res not in f:
            ans_f.append(res*10/denominator)
            f.append(res)
            res = res*10 % denominator    
        print f, ans_f
        if res == 0:
            if not ans_f: 
                if flag == 1:
                    return str(i)
                else:
                    return '-' + str(i)
            else:
                if flag == 1:
                    return str(i)+'.'+''.join(map(str,ans_f))
                else:
                    return  '-'+str(i)+'.'+''.join(map(str,ans_f))
        if res in f:
            notrec = ans_f[:f.index(res)]
            rec = ans_f[f.index(res):]
            if flag == 1:
                return str(i)+'.'+''.join(map(str,notrec))+'('+''.join(map(str,rec))+')'
            else:
                return '-'+str(i)+'.'+''.join(map(str,notrec))+'('+''.join(map(str,rec))+')'
            
numerator = 177
denominator = 17
s = Solution()
s.fractionToDecimal(numerator, denominator)

