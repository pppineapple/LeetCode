# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 07:52:46 2018

@author: xiaohong
"""

'''
二进制求和
'''
 
'''
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
'''

'''
我的 44ms
'''


def addBinary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        if len(a) >= len(b):
            long = a
            short = b            
        else:
            short = a
            long = b
            
        output = ''    
        forward = 0
        for i in range(len(long)):
            if i < len(short):
                summ = int(short[-1-i]) + int(long[-1-i]) + forward
            else:
                summ = int(long[-1-i]) + forward
            if summ == 3:
                summ = 1
                forward = 1
            elif summ == 2:
                summ = 0
                forward = 1
            else:
                forward = 0   
            output = str(summ) + output
                
        if forward == 1:
            output = '1' + output
        return output


'''
best 24ms 用了int(char, 进制参数)， bin(将10进制转为2进制)
'''                       
def addBinary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a_10 = int(a, 2)
        b_10 = int(b, 2)
        c = a_10 + b_10
        return bin(c)[2:]
    
addBinary('1010','111')    
    


