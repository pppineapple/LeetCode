#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 18:26:33 2018

@author: pineapple
"""

'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，
且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

'''
我的：　时间复杂度O(n) 空间复杂度O(n^2)
思路：按照已知矩阵，然后螺旋打印出来的那道题的思路：
    先建立矩阵的形状，再把要填的数字用数组表示，
    注意要反转，然后用pop来取数字
    然后根据题意顺时针，往里面填数字
    建立top,bottom,left,right四指针来遍历
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0]*n for i in range(n)]
        top, bottom, left, right = 0, n, 0, n
        nlist = [i for i in range(1, n**2+1)]
        nlist.reverse()
        while top < bottom and left < right:
            for i in range(left, right):
                result[top][i] = nlist.pop()
            for j in range(top+1, bottom):
                result[j][right-1] = nlist.pop()
            for x in range(right-1-1, left-1, -1):
                if bottom - top > 1:
                    result[bottom-1][x] = nlist.pop()
            for y in range(bottom-1-1, top, -1):
                if right - left > 1:
                    result[y][left] = nlist.pop()
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return result
    
n = 3
