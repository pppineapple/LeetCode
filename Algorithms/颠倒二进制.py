# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:18:16 2018

@author: xiaohong
"""

'''
颠倒给定的 32 位无符号整数的二进制位。

示例:

输入: 43261596
输出: 964176192
解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
     返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
进阶:
如果多次调用这个函数，你将如何优化你的算法？
'''

'''
我的 0.62
思路 转化为2进制，然后利用2进制直接计算10进制 ，注意要补齐32位
'''



def reverseBits(n):
        nlist = []
        while n > 0:
            res = n % 2
            n = n // 2
            nlist.append(res)
        while len(nlist) < 32:
            nlist.append(0)

        output = 0        
        for i in range(len(nlist)):
            output +=  nlist[i] * 2 ** (len(nlist)-1-i)
            
        return output
    
