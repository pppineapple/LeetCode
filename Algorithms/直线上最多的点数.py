#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:50:45 2018

@author: pineapple
"""


'''
别人的: 时间复杂度O(n^2)　空间复杂度Ｏ(n)
思路：两点可以确定一条直线，那么选择固定一个点，求其他点与固定点的斜率，
　　如果斜率相同，那么斜率相同的点在同一条直线上。
  　同时要考虑，斜率可能为无穷大，也有可能两个点为同一个点。
   键值应该为：斜率。
   同时也要考虑他会给出一些坐标相同的点，


'''
import numpy as np
# Definition for a point.
class Point(object):
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

class Solution(object):

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)
        result = 0
        
        for i in points:
            slope = {'inf':0}
            samepoint = 1
            for j in points:
                
                if i == j:
                    continue
                elif i.x == j.x and i.y != j.y:
                    slope['inf'] += 1
                elif i.x != j.x:
                    k = np.longdouble(1) * (i.y-j.y)/(i.x-j.x)
                    slope[k] = slope.get(k, 0) + 1
                else:
                    samepoint += 1
            result = max(result, max(slope.values())+ samepoint)
        return result

    
p1 = Point(0,0)
p2 = Point(1,1)
p3 = Point(0,0)
points = [p1,p2,p3]
s = Solution()
s.maxPoints(points)