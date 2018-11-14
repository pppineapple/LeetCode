# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:55:18 2018

@author: xiaohong
"""

'''
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:
输入: 6
输出: true
解释: 6 = 2 × 3

示例 2:
输入: 8
输出: true
解释: 8 = 2 × 2 × 2

示例 3:
输入: 14
输出: false 
解释: 14 不是丑数，因为它包含了另外一个质因数 7。
说明：

1 是丑数。
输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。
'''

'''
我的 0.96
思路 递归
'''

def isUgly(num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False        
        if num == 1 or num == 2 or num == 3 or num == 5:
            return True
        nlist = [2, 3, 5]
        
        for n in nlist:
            res = num % n
            numshoter = num // n            
            if res == 0:
                return isUgly(numshoter)
        return False
    
    
