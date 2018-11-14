# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:56:40 2018

@author: xiaohong
"""

'''
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:

n = 5

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤

因为第三行不完整，所以返回2.
示例 2:

n = 8

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

因为第四行不完整，所以返回3.
'''

'''
我的 0.22
思路； 遍历
'''
def arrangeCoins(n):
        """
        :type n: int
        :rtype: int
        """

        floor = 0
        floor_num = 1
        while n >= floor_num:
            n = n - floor_num
            floor_num += 1
            floor += 1
        return floor
    
    
arrangeCoins(5)

'''
由等差数列求和公式：
x ^ 2 + x = 2 * n 解得
x = sqrt(2 * n + 1/4) - 1/2
'''
def arrangeCoins(n):
        """
        :type n: int
        :rtype: int
        """
        return int((2*n+0.25)**0.5-0.5)





