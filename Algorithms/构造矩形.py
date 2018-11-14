#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 08:46:13 2018

@author: pineapple
"""

'''
作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 
现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W 
且满足以下要求的矩形的页面。要求：

1. 你设计的矩形页面必须等于给定的目标面积。

2. 宽度 W 不应大于长度 L，换言之，要求 L >= W 。

3. 长度 L 和宽度 W 之间的差距应当尽可能小。
你需要按顺序输出你设计的页面的长度 L 和宽度 W。

示例：
输入: 4
输出: [2, 2]
解释: 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。
但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 
所以输出长度 L 为 2， 宽度 W 为 2。

说明:
给定的面积不大于 10,000,000 且为正整数。
你设计的页面的长度和宽度必须都是正整数。
'''

'''
我的：　时间复杂度Ｏ(logn), 空间复杂度Ｏ(1)
思路：　直接来看 area　能是哪些数的乘积，
    这里有个窍门，只要商大于除数就应该跳出循环，
    因为接下来就只是和前面重复了，只是商变成了除数，除数变成了商
    在本题中要求L大于等于W，所以从ｗ=1开始，拿area去除以ｗ
    这时的Ｌ肯定都比Ｗ大，如果Ｌ比Ｗ小了，就跳出循环
    然后设置一个变量用来比较和保存最小的Ｌ-Ｗ间隔，再设置一个变量
    来保存输出的结果result
'''


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = 1
        l = area // w
        diff = area
        result = None
        while l>=w:
            if area % w == 0:
                if diff > area//w-w:
                    diff = area//w - w
                    result = [area//w, w]            
            w += 1
            l = area // w
        return result
area = 2
area = 9999997
s = Solution()
s.constructRectangle(area)

