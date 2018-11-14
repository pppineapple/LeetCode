#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 09:04:44 2018

@author: pineapple
"""

'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。



输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，
容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''


'''
别人的：　时间复杂度O(n) 空间复杂度O(1)
思路：双指针对撞，用一个vmax变量来保存最大的体积
    然后双指针按照高度低的指针向高度高的指针方向移动
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        vmax = 0
        left = 0
        right = len(height) - 1
        while left < right :
            v =  min(height[left], height[right]) * (right-left)
            vmax = max(v, vmax)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return vmax
    
    
'''
第二次做
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxv = 0
        left = 0
        right = len(height)-1
        while left < right:
            v = (right-left) * min(height[right], height[left])
            maxv = max(v, maxv)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxv
            