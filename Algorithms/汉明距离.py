#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 11:36:37 2018

@author: pineapple
"""
'''
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。
'''

'''
我的：　时间复杂度O(n) 空间复杂度O(n)
思路：　将x,y转化为二进制，因为可能x,y二进制长短不一，所以用列表储存
    并且要将短的列表补０直到两个列表长度相同。
    然后比较不同的位置，返回计数
'''


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xlist = []
        ylist = []
        while x > 0:
            xres = x % 2
            x = x//2
            xlist.append(xres)
        while y > 0:
            yres = y % 2
            y = y//2
            ylist.append(yres)
            
        if len(xlist) < len(ylist):
            for _ in range(len(ylist)-len(xlist)):
                xlist.append(0)
        else:
            for _ in range(len(xlist)-len(ylist)):
                ylist.append(0)            
                
        dist = 0
        for u in range(len(xlist)):
            if xlist[u] != ylist[u]:
                dist += 1
        return dist