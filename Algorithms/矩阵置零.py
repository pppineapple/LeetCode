#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:44:03 2018

@author: pineapple
"""

'''
给定一个 m x n 的矩阵，如果一个元素为 0，
则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？
'''

'''
别人的：时间复杂度O(n^2) 空间复杂度O(c)
思路：把有0的元素映射到首行和首列，然后将首行首列中出现0的行和列置为0
    首先遍历一下首行首列,用变量fr_zero和fc_zero来表示首行首列是否出现了0
    然后将非首行非首列的元素0映射到首行和首列
    然后将非首行和非首列的元素中，对应与首行首列为0的值置为0
    最后来看fr_zero和fc_zero是否为True
    如果是：然后就将首行或者首列置为０
    
'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 先判断首行首列是否含0
        fr_zero = False
        fc_zero = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                fc_zero = True
                break
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                fr_zero = True
                break
        # 将非首行非首列元素0映射到首行和首列       
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # 将非首行和非首列的元素中，对应与首行首列为0的值置为0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                #print matrix[i][j], matrix[i][0], matrix[0][j]
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # 根据前面统计的首行首列是否为零，更新首行首列
        if fc_zero:
            for i in range(len(matrix)):
                if matrix[i][0] == 0:
                    for j in range(len(matrix)):
                        matrix[j][0] = 0
                    break
        if fr_zero:
            for j in range(len(matrix[0])):
                if matrix[0][j] == 0:
                    matrix[0] = [0] * len(matrix[0])
                    break
        
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[1,1,1],[1,0,1],[1,1,1]]

