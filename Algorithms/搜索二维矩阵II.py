#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:04:27 2018

@author: pineapple
"""

'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。
该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。


'''

'''
逐行二分查找 时间复杂度O(nlogm) 空间复杂度O(1)
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        for i in range(len(matrix)):
            left, right = 0, len(matrix[0])-1
            mid = (left+right)//2
            while left <= right:
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    left = mid + 1
                elif matrix[i][mid] > target:
                    right = mid - 1
                mid = (left+right)//2
        return False

'''
分治法：时间复杂度O(max(m,n)) 空间复杂度O(0)
思路：matrix[len(matrix)-1][0]即矩阵左下角的值有特殊含义
    １．这个值是第一列的最大值
    ２．这个值是最后一行的最小值
    如果 matrix[len(matrix)-1][0] < target:
        说明target的值不在最后一行，就可以去除最后一行 i-=1
    如果 matrix[len(matrix)-1][0] > target:
        说明target的值不在第一列，就可以去除最第一列 j+=1    
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """        
        if matrix == [] or matrix == [[]]:
            return False
        i = len(matrix)-1
        j = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
        return False            
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
matrix[:3][1:]
