#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 14:33:42 2018

@author: pineapple
"""



'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），
请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return matrix
        result = []
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)
        
        while left < right and top < bottom:
            for i in range(left, right):
                result.append(matrix[top][i])
                
            for j in range(top+1, bottom):
                result.append(matrix[j][right-1])
                
            for x in range(right-2, left-1, -1): 
                if bottom - top > 1:
                    result.append(matrix[bottom-1][x])
                
            for y in range(bottom-2, top, -1):
                if right - left > 1:
                    result.append(matrix[y][left])
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return result
 
matrix = [[7],[9],[6]]
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
 [10,11,12 ]
]
s = Solution()
s.spiralOrder(matrix)


'''
第二次做
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        left, top = 0, 0
        right, bottom = len(matrix[0])-1, len(matrix)-1
        ans = []
        while True:
            if left <= right and top <= bottom:
                for i in range(left, right+1):
                    ans.append(matrix[top][i])
                top += 1
                cur_c = right
            else:
                break
            if left <= right and top <= bottom:
                for j in range(top, bottom+1):
                    ans.append(matrix[j][cur_c])
                right -= 1
                cur_r = bottom
            else:
                break
            if left <= right and top <= bottom:
                for i in range(right, left-1, -1):
                    ans.append(matrix[cur_r][i])
                bottom -= 1
                cur_c = left
            else:
                break
            
            if left <= right and top <= bottom:
                for j in range(bottom, top-1, -1):
                    ans.append(matrix[j][cur_c])
                left += 1
                cur_r = top
            else:
                break
        return ans